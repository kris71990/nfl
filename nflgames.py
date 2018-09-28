# nflgames.py 
# gets nfl weekly matchups and enters them into spreadsheet along with
# team records from nflteams.py

import requests, bs4, openpyxl, os, sys, re, nflteams, byeteams

week_num = sys.argv[1]

if isinstance(week_num, str):
   week_num = week_num.split(' ')[1]

# get weekly matchup data
url = 'http://www.vegasinsider.com/nfl/odds/las-vegas/'
res = requests.get(url)
res.raise_for_status()

# find and parse soup for game matchups
def findMatchups():
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  teams_html = soup.select('.tabletext')
  teams_raw = []

  for item in teams_html:
    team = item.getText()
    teams_raw.append(team)

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

matchups = findMatchups()
odds = findOdds()

# creates dictionary from matchup/odds data 
def createDict():
  data = {}
  keys = range(len(matchups))

  for i in keys:
    data[i] = { matchups[i] : None }

  for i in keys:
    teams = matchups[i].split(' at ')

    # if home team is favoured
    if re.search('u', odds[i].split('-', 2)[0]):
      rx = re.compile(r'([a-zA-Z\s.-]+)', re.I)
      t = rx.search(teams[1]).group(0)
      line = '-'.join(odds[i].split('-', 2)[2:]).split('-')[0].replace('EV', '')
      data[i][matchups[i]] = odds[i]
      print('%s -%s' % (t, line))
    
    # if road team is favoured
    else:
      rx = re.compile(r'([a-zA-Z\s.-]+)', re.I)
      t = rx.search(teams[0]).group(0)
      line = '-'.join(odds[i].split('-', 2)[:2])
      data[i][matchups[i]] = odds[i]
      print('%s %s' % (t, line))

  print('\n')
  return data

# Print all weekly game information to console
print('\nGames for Week %s\n' % (week_num))
print(createDict())
print('\n')
print(byeteams.get_bye_teams(week_num))

# open spreadsheet and write info
def write_game_info():
  os.chdir('/Users/kris/Desktop')
  wb = openpyxl.load_workbook('2018picksxl.xlsx')
  sheet = wb.get_sheet_by_name('Sheet 1')

  #find spreadsheet start row and write game info to appropriate cells
  write_matchup_num = 0
  start_row = 0
  start_week = sys.argv[1]

  for cell in sheet.columns[0]:
    if cell.value == start_week:
      start_row += 2
      for row_num in range(start_row, len(matchups) + start_row):
        game = sheet.cell(row=row_num, column=1)
        game.value = matchups[write_matchup_num]
        write_matchup_num += 1       
    else: 
      start_row += 1
  
  wb.save('2018picksxlnew.xlsx')