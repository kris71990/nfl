# nflteams.py 
# gets team records and stores them in a dictionary
# nflgames.py imports this file to include team records in matchup data to be entered into spreadsheet

from assets import soup

def get_team_records():
  matchups_soup = soup.get_matchups_soup()
  # teams_html = matchups_soup.select('.viCellBg2.cellBorderL1.cellTextNorm.padLeft')
  teams_html = matchups_soup.select('td')
  teams_dict = {}

  for x in range(0, len(teams_html), 5):
    team = teams_html[x].get_text()
    record = teams_html[x + 1].get_text()

    # reformat NY and LA
    if 'LA' in team or 'NY' in team:
      team_split = team.split(' ')
      city = '.'.join(list(team_split[0]))
      team = city + '. ' + team_split[1]

    # if no ties, slice tie column off
    if record.split('-')[2] == '0':
      record = '-'.join(record.split('-')[:-1])
    teams_dict[team] = record
  
  return teams_dict
