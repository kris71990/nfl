import unittest
from schedule import nflgames, byeteams, nflteams
from assets import soup

class TestTeams(unittest.TestCase):
  def test_team_records(self):
    records = nflteams.get_team_records()
    self.assertIs(type(records), dict)
    self.assertEqual(len([*records]), 32)

class TestByes(unittest.TestCase):
  def test_bye_teams(self):
    byes = byeteams.get_bye_teams('2')

    if byes is None:
      self.assertIsNone(byes)
    else:
      self.assertIs(type(byes), list)

  def test_format_byes(self):
    byes = byeteams.get_bye_teams('2')
    formatted_byes = byeteams.format_byes(byes)
    
    if byes is None:
      self.assertIsNone(formatted_byes)
    else:
      self.assertIs(type(formatted_byes), str)

class TestMatchups(unittest.TestCase):
  def test_find_matchups(self):
    byes = byeteams.get_bye_teams('2')
    odds_soup = soup.get_odds_soup()
    matchups = nflgames.find_matchups(byes, odds_soup)

    bye_number = len(byes) if byes else 0
    self.assertIs(type(matchups), list)
    self.assertEqual(len(matchups), 16 - (bye_number / 2))

  def test_find_odds(self):
    byes = byeteams.get_bye_teams('2')
    bye_number = len(byes) if byes else 0
    odds_soup = soup.get_odds_soup()
    odds = nflgames.find_odds(odds_soup)

    self.assertIs(type(odds), list)
    self.assertIs(type(odds[0]), dict)
    self.assertEqual(len(odds), 16 - (bye_number / 2))

  def test_game_data(self):
    byes = byeteams.get_bye_teams('2')
    odds_soup = soup.get_odds_soup()
    matchups = nflgames.find_matchups(byes, odds_soup)
    odds = nflgames.find_odds(odds_soup)

    games = nflgames.create_game_data(matchups, odds)
    self.assertIs(type(games), dict)
    self.assertIs(type(games[0]), dict)
    self.assertIs(type(list(games[0].keys())[0]), str)
    self.assertIs(type(list(games[0].values())[0]), str)

if __name__ == '__main__':
  unittest.main()