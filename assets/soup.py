import requests
from bs4 import BeautifulSoup

# get scores soup per week
def get_scores_soup(week, season_type):
  url = 'http://www.espn.com/nfl/schedule/_/week/' + week + '/seasontype/' + season_type
  # ESPN requires a User-Agent header in the request
  hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
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

def convert_espn(week):
  if int(week) > 18:
    espn_season_type = '3'
    espn_week = str(int(week) - 18)
  else:
    espn_season_type = '2'
    espn_week = week
  
  return { 'espn_week': espn_week, 'espn_season_type': espn_season_type }
