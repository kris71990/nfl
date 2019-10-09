# nflgames.py 
# gets nfl weekly matchups and enters them into spreadsheet along with
# team records from nflteams.py

import requests, bs4, openpyxl, os, sys, re, nflteams, byeteams, teaminfo
from dotenv import load_dotenv
load_dotenv()

week_num = sys.argv[1]

if 'Week' in week_num:
  week_num = week_num.split(' ')[1]

# get weekly matchup data
url = 'http://www.vegasinsider.com/nfl/odds/las-vegas/'
res = requests.get(url)
res.raise_for_status()

# find and parse soup for game matchups
def findMatchups(byes):
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  teams_html = soup.select('a[class=tabletext]')
  teams_raw = []

  for item in teams_html:
    team = item.getText()
    teams_raw.append(team)

  # cut list down to accomodate extra games website is now displaying
  total_active_teams = 32 - len(byes) 
  teams_raw = teams_raw[:total_active_teams]

  # create the matchups from teams_raw list
  matchups = []
  matchup_num = 0
  matchup_num_2 = matchup_num + 1
  num_games = int(len(teams_raw) / 2)
  dict = nflteams.team_records_dict 

  for i in range(0, num_games):
    matchups.append(teams_raw[matchup_num] + ' ' + dict.get(teams_raw[matchup_num]) + \
    ' at ' + teams_raw[matchup_num_2] + ' ' + dict.get(teams_raw[matchup_num_2]))
    matchup_num += 2
    matchup_num_2 += 2

  return matchups

# finds odds soup and parses it to find the VI consensus for every matchup
def findOdds():
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  odds_html = soup.findAll('a', class_=['cellTextNorm', 'cellTextHot'])
  odds = []

  for x in range(1, len(odds_html), 9):
    game_odd = odds_html[x].find('br').getText()
    game_odd = game_odd.replace('\t', '').replace('\n', '').replace('\xa0', '')
    odds.append(game_odd)
  
  return odds

byeData = byeteams.get_bye_teams(week_num)
formattedByes = byeteams.formatByes(byeData)
matchups = findMatchups(byeData)
odds = findOdds()

# creates dictionary from matchup/odds data 
def createGameData():
  data = {}
  keys = range(len(matchups))

  for i in keys:
    data[i] = { matchups[i] : None }

  for i in keys:
    teams = matchups[i].split(' at ')

    # if home team is favoured
    if re.search('u', odds[i].split('-', 2)[0]):
      rx = re.compile(r'([a-zA-Z\s.-]+)', re.I)
      t = rx.search(teams[1]).group(0).strip()
      t = teaminfo.abbreviations[t]

      line = '-'.join(odds[i].split('-', 2)[2:]).split('-')[0].replace('EV', '')
      lineClean = '%s -%s' % (t, line)
      data[i][matchups[i]] = lineClean
      print(lineClean)
    
    # if road team is favoured
    else:
      rx = re.compile(r'([a-zA-Z\s.-]+)', re.I)
      rx2 = re.compile(r'([EV].+)', re.I)
      t = rx.search(teams[0]).group(0).strip()
      t = teaminfo.abbreviations[t]

      line = '-'.join(odds[i].split('-', 2)[:2])

      if rx2.search(line):
        index = line.index(rx2.search(line).group(0))
        line = line[0 : index]

      lineClean = '%s %s' % (t, line)
      data[i][matchups[i]] = lineClean
      print(lineClean)

  print('\n')
  return data

# Print all weekly game information to console
print('\nGames for Week %s\n' % (week_num))
gameData = createGameData()
print(gameData)
print('\n')
print(formattedByes)

# open spreadsheet and write info
def write_game_info():
  print('\nWriting to spreadsheet...\n')

  os.chdir(os.getenv('DESKTOP'))
  wb = openpyxl.load_workbook(os.getenv('EXCEL_FILE'))
  sheet = wb.get_sheet_by_name('Sheet 1')

  #find spreadsheet start row and write game info to appropriate cells
  write_matchup_num = 0
  start_row = 0
  start_week = sys.argv[1]
  bye_row = 0

  for cell in sheet.columns[0]:
    if cell.value == start_week:
      start_row += 2
      for row_num in range(start_row, len(matchups) + start_row):
        game = sheet.cell(row=row_num, column=1)

        if (row_num == (len(matchups) + start_row) - 1):
          bye_row = row_num

        game.value = matchups[write_matchup_num]

        line = sheet.cell(row=row_num, column=2)
        line.value = gameData[write_matchup_num][matchups[write_matchup_num]]
        write_matchup_num += 1       
    else: 
      start_row += 1
  
  bye = sheet.cell(row=bye_row+1, column=1)
  bye.value = formattedByes

  week = sheet.cell(row=bye_row+1, column=3)
  week.value = 'Week =>'

  total = sheet.cell(row=bye_row+2, column=3)
  total.value = 'Total =>'

  print('Done')
  wb.save(os.getenv('EXCEL_FILE_NEW'))

write_game_info()