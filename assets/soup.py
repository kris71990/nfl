import requests
from bs4 import BeautifulSoup

# get scores soup per week
def get_scores_soup(week):
  url = 'http://www.espn.com/nfl/schedule/_/week/' + week
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'html.parser')
  return soup

# get matchups soup with records
def get_matchups_soup():
  # url = 'http://www.vegasinsider.com/nfl/matchups/'
  url = 'https://www.teamrankings.com/nfl/trends/win_trends/'
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'html.parser')
  return soup

# get odds soup
def get_odds_soup():
  url = 'http://www.vegasinsider.com/nfl/odds/las-vegas/'
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'html.parser')
  return soup
