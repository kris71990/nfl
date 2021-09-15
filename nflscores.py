# nflscores.py 
# gets nfl weekly scores and enters them into spreadsheet 

import requests, bs4, openpyxl, os, sys, re, nflteams, byeteams, teaminfo, weekInfo
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
    score_split = score.split(' ')
    scores[score_split[0]] = '%s-%s' % (score_split[1].strip(','), score_split[3])

  print(scores)
  return scores

get_scores(week_num)