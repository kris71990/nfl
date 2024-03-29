import sys
from schedule import nflgames, nflteams
from results import nflscores
from spreadsheet import actions
from dotenv import load_dotenv

load_dotenv()

action = sys.argv[1]

if len(sys.argv) < 3:
  if action == 'teams': 
    teams = nflteams.get_team_records()
    print('\nPower Rankings\n')
    for key, value in teams.items():
      if len(key) < 8:
        print(key + '\t\t' + value)
      else:
        print(key + '\t' + value)
  print('\nDone')
else:
  week = sys.argv[2]
  if 'Week' in week:
    week = week.split(' ')[1]

  if action == 'scores++': # scores and schedule of next week
    ss = actions.load_spreadsheet()
    nflscores.write_scores(ss, week, True)

    next_week = int(week) + 1
    if next_week < 23:
      nflgames.init(ss, str(next_week))

    actions.save_spreadsheet(ss['wb'])
  elif action == 'schedule': # schedule of next week
    ss = actions.load_spreadsheet()
    nflgames.init(ss, week)
    actions.save_spreadsheet(ss['wb'])
  elif action == 'scores+': # scores plus tally scores
    ss = actions.load_spreadsheet()
    nflscores.write_scores(ss, week, True)
    actions.save_spreadsheet(ss['wb'])
  elif action == 'scores': # just scores
    ss = actions.load_spreadsheet()
    nflscores.write_scores(ss, week, False)
    actions.save_spreadsheet(ss['wb'])
  else:
    print('Done')

