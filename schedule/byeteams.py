# byeteams.py
# accesses weekly schedule and identifies bye teams

from assets import soup

def get_bye_teams(week):
  espn_format = soup.convert_espn(week)

  schedule_soup = soup.get_scores_soup(espn_format['espn_week'], espn_format['espn_season_type'])
  bye_teams_html = schedule_soup.select('.pr6')
  bye_teams = []

  for each in bye_teams_html:
    team = each.getText()
    bye_teams.append(team)

  if bye_teams_html:
    return bye_teams
  else:
    return None

def format_byes(bye_teams):
  if bye_teams is None: 
    return None

  bye_string = '*Bye - '
  count = 0
  for each in range(0, len(bye_teams)):
    count += 1
    if count == len(bye_teams):
      bye_string += bye_teams[each]
    else:
      bye_string += bye_teams[each] + ', '
  return bye_string
  