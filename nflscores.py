# nflscores.py 
# gets nfl weekly scores and enters them into spreadsheet 

import requests, bs4, openpyxl, os, sys, re, teaminfo, weekInfo
from dotenv import load_dotenv
load_dotenv()

week_num = sys.argv[1]

if 'Week' in week_num:
  week_num = week_num.split(' ')[1]

def get_scores(week):
  url = 'http://www.espn.com/nfl/schedule/_/week/' + week
  res = requests.get(url)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  scores_raw = soup.find_all('a', { 'name': '&lpos=nfl:schedule:score' })
  scores = {}

  for each in scores_raw:
    score = each.getText()
    print(score)
    score_split = score.split(' ')
    # if tie *** may be buggy ***
    if (score_split[1].strip(', ') == score_split[3]):
      scores[score_split[0] + '-' + scores[score_split[2]]] = '%s-%s' % (score_split[1].strip(','), score_split[3])
    else:
      # if overtime, add OT to string
      if (len(score_split) > 4):
        scores[score_split[0]] = '%s-%s %s' % (score_split[1].strip(','), score_split[3], score_split[4])
      else:
        scores[score_split[0]] = '%s-%s' % (score_split[1].strip(','), score_split[3])

  return scores

def write_scores(week):
  print('\nWriting to spreadsheet...\n')

  print('Week 1 results:\n')
  scores = get_scores(week)

  os.chdir(os.getenv('DESKTOP'))
  wb = openpyxl.load_workbook(os.getenv('EXCEL_FILE'))
  sheet = wb.get_sheet_by_name('Sheet 1')

  # find spreadsheet start row and write scores to appropriate cells
  write_score_index = 0
  start_row = 0
  if 'Week' not in week_num:
    if (int(week_num) > 17):
      start_week = weekInfo.playoff_week_titles[week_num]
    else:
      start_week = 'Week ' + week_num
  else:
    start_week = week_num

  for cell in sheet.columns[0]:
    if cell.value == start_week:
      start_row += 2
      for row_num in range(start_row, len(scores) + start_row):
        score_cell = sheet.cell(row=row_num, column=3)
        matchup_cell = sheet.cell(row=row_num, column=1)
        matchup_cell_text = matchup_cell.value

        rx = re.compile(r'([a-zA-Z\s.]+)', re.I)
        teams_raw = rx.findall(matchup_cell_text)
        teams = [x.strip(' ') for x in teams_raw]
        team1abbr = teaminfo.abbreviations[teams[0]].upper()
        team2abbr = teaminfo.abbreviations[teams[1][3:]].upper()
        
        if (team1abbr in scores):
          score_cell.value = '%s %s' % (team1abbr, scores[team1abbr])
        elif (team2abbr in scores):
          score_cell.value = '%s %s' % (team2abbr, scores[team2abbr])
        write_score_index += 1       
    else: 
      start_row += 1

  wb.save(os.getenv('EXCEL_FILE_NEW'))
  print('Done')

write_scores(week_num)
