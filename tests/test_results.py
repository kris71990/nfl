import unittest
from results import nflscores
from assets import soup

class TestScores(unittest.TestCase):
  def test_get_scores(self):
    scores = nflscores.get_scores('1')
    self.assertIs(type(scores), dict)
    self.assertIs(type(list(scores.keys())[0]), str)
    self.assertIs(type(list(scores.values())[0]), str)

if __name__ == '__main__':
  unittest.main()