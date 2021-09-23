import requests, bs4

# get scores soup per week
def get_scores_soup(week):
  url = 'http://www.espn.com/nfl/schedule/_/week/' + week
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  return soup

# get matchups soup with records
def get_matchups_soup():
  url = 'http://www.vegasinsider.com/nfl/matchups/'
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  return soup

# get odds soup
def get_odds_soup():
  url = 'http://www.vegasinsider.com/nfl/odds/las-vegas/'
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  return soup
