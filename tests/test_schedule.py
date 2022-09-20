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
    byes = byeteams.get_bye_teams('3')

    if byes is None:
      self.assertIsNone(byes)
    else:
      self.assertIs(type(byes), list)

  def test_format_byes(self):
    byes = byeteams.get_bye_teams('3')
    formatted_byes = byeteams.format_byes(byes)
    
    if byes is None:
      self.assertIsNone(formatted_byes)
    else:
      self.assertIs(type(formatted_byes), str)

class TestMatchups(unittest.TestCase):
  def test_find_matchups(self):
    byes = byeteams.get_bye_teams('3')
    odds_soup = soup.get_odds_soup()
    matchups = nflgames.find_matchups(byes, odds_soup)

    bye_number = len(byes) if byes else 0
    self.assertIs(type(matchups), list)
    self.assertEqual(len(matchups), 16 - (bye_number / 2))

if __name__ == '__main__':
  unittest.main()