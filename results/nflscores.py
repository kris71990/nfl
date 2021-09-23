# nflscores.py 
# gets nfl weekly scores and enters them into spreadsheet 

import os, re, results.tallyscores
from assets import teaminfo, weekInfo, soup
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment

def get_scores(week):
  scores_soup = soup.get_scores_soup(week)
  scores_raw = scores_soup.find_all('a', { 'name': '&lpos=nfl:schedule:score' })
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

  os.chdir(os.getenv('LOCATION'))
  wb = load_workbook(os.getenv('EXCEL_FILE'))
  sheet = wb.get_sheet_by_name('Sheet 1')

  # find spreadsheet start row and write scores to appropriate cells
  write_score_index = 0
  start_row = 0
  if int(week) > 17:
    start_week = weekInfo.playoff_week_titles[week]
  else:
    start_week = 'Week ' + week

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
          score = '%s %s' % (team1abbr, scores[team1abbr])
          score_cell.value = score
          score_cell.font = Font(name='Times New Roman', size=12)
          score_cell.alignment = Alignment(horizontal='center', vertical='center')
        elif (team2abbr in scores):
          score = '%s %s' % (team2abbr, scores[team2abbr])
          score_cell.value = score
          score_cell.font = Font(name='Times New Roman', size=12)
          score_cell.alignment = Alignment(horizontal='center', vertical='center')
        results.tallyscores.color_fill(sheet, score, row_num)
        write_score_index += 1       
    else: 
      start_row += 1

  wb.save(os.getenv('EXCEL_FILE_NEW'))
  print('Done')