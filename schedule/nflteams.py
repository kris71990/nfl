# nflteams.py 
# gets team records and stores them in a dictionary
# nflgames.py imports this file to include team records in matchup data to be entered into spreadsheet

from assets import soup

def get_team_records():
  matchups_soup = soup.get_matchups_soup()
  teams_html = matchups_soup.select('.viCellBg2.cellBorderL1.cellTextNorm.padLeft')
  teams_raw = []

  delete_stuff = 0
  for item in teams_html:
    team = item.getText()
    team1 = team.replace('\n', '')
    team2 = team1.replace('\t', '')
    team3 = team2.replace('\r', '')
    team4 = team3.replace('\xa0', '')
    if delete_stuff % 3 == 0:
      team5 = team4[4:]
      teams_raw.append(team5)
    elif delete_stuff % 3 == 1:
      team6 = team4.split(' ')[0]
      teams_raw.append(team6)
    else:
      del team4
    delete_stuff += 1

  team_records_dict = {
    teams_raw[i]: teams_raw[i+1] for i in range(0, len(teams_raw), 2)
  }
  
  return team_records_dict
