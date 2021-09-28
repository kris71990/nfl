# byeteams.py
# accesses weekly schedule and identifies bye teams

from assets import soup

def get_bye_teams(week):
  schedule_soup = soup.get_scores_soup(week)
  bye_teams_html = schedule_soup.select('.odd.byeweek a span')
  bye_teams = []

  for each in bye_teams_html:
    team = each.getText()
    bye_teams.append(team)

  return bye_teams

def format_byes(bye_teams):
  if len(bye_teams) is 0: 
    return 'No bye teams'

  bye_string = '* Bye - '
  count = 0
  for each in range(0, len(bye_teams)):
    count += 1
    if count == len(bye_teams):
      bye_string += bye_teams[each]
    else:
      bye_string += bye_teams[each] + ', '
  return bye_string
  