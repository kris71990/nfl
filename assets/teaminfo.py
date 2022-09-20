# teaminfo.py
# a dictionary of teams and their abbreviation, to be utilized in spreadsheet insertion
# helper functions to translate between team name formats

abbreviations = {
  'Miami' : 'Mia',
  'New England' : 'NE',
  'Houston' : 'Hou',
  'Indianapolis' : 'Ind',
  'Cincinnati' : 'Cin',
  'Atlanta' : 'Atl',
  'Buffalo' : 'Buf',
  'Green Bay' : 'GB',
  'Detroit' : 'Det',
  'Dallas' : 'Dal',
  'N.Y. Jets' : 'NYJ',
  'Jacksonville' : 'Jax',
  'Tampa Bay' : 'TB',
  'Chicago' : 'Chi',
  'Philadelphia' : 'Phi',
  'Tennessee' : 'Ten',
  'Seattle' : 'Sea',
  'Arizona' : 'Ari',
  'Cleveland' : 'Cle',
  'Las Vegas' : 'LV',
  'San Francisco' : 'SF',
  'L.A. Chargers' : 'LAC',
  'L.A. Rams' : 'LAR',
  'Minnesota' : 'Min',
  'New Orleans' : 'NO',
  'N.Y. Giants' : 'NYG',
  'Baltimore' : 'Bal',
  'Pittsburgh' : 'Pit',
  'Kansas City' : 'KC',
  'Denver' : 'Den',
  'Washington' : 'Wsh',
  'Carolina' : 'Car'
}

def reformat_without_nickname(team):
  team_split = team.split(' ')

  if team_split[1] == 'York' or team_split[1] == 'Angeles':
    reformatted_team = reformat_city_multiple_teams(team_split)
    return reformatted_team

  if len(team_split) > 2:
    reformatted_team = ' '.join(team_split[:2])
  else:
    reformatted_team = team_split[0]
  return reformatted_team

def reformat_city_multiple_teams(team_split):
  city = team_split[0][0] + '.' + team_split[1][0] + '.'
  reformatted_team = city + ' ' + team_split[2]
  return reformatted_team