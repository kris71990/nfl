# teaminfo.pu
# a dictionary of teams and their abbreviation, to be utilized in spreadsheet insertion

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

# Patterns
# - Normal: first three letters
# - With Space : first letter of each word
# - With Period : letters between periods, plus first letter of following word
# - Two same letters in a row (Minn, Tenn, Pitt, Buff) : include both letters
# - Logical Oddballs (Balt, Wash, Az, Jax) : ...