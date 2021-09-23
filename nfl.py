import sys
from schedule import nflgames
from results import nflscores
from dotenv import load_dotenv

load_dotenv()

action = sys.argv[1]
week = sys.argv[2]

if 'Week' in week:
  week = week.split(' ')[1]

if action == 'schedule':
  nflgames.init(week)
elif action == 'scores':
  nflscores.write_scores(week)
else:
  print('Done')
