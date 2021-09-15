# byeteams.py
# accesses weekly schedule and identifies bye teams

import requests, bs4

def get_bye_teams(week):
  url = 'http://www.espn.com/nfl/schedule/_/week/' + week
  res = requests.get(url)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  bye_teams_html = soup.select('.odd.byeweek a span')
  bye_teams = []

  for each in bye_teams_html:
    team = each.getText()
    bye_teams.append(team)

  return bye_teams

def formatByes(bye_teams):
  if len(bye_teams) is 0: 
    return None

  bye_string = '* Bye - '
  count = 0
  for each in range(0, len(bye_teams)):
    count += 1
    if count == len(bye_teams):
      bye_string += bye_teams[each]
    else:
      bye_string += bye_teams[each] + ', '
  return bye_string
  