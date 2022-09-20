import unittest
import sys
from assets import soup

class TestSoup(unittest.TestCase):
  def test_espn_convert(self):
    espn = soup.convert_espn('1')
    self.assertIs(type(espn['espn_week']), str)
    self.assertIs(type(espn['espn_season_type']), str)

  def test_scores_soup(self):
    espn = soup.convert_espn('1')
    data = soup.get_scores_soup(espn['espn_week'], espn['espn_season_type'])
    self.assertTrue(data.body)

if __name__ == '__main__':
  unittest.main()