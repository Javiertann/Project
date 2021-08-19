import unittest
from main import stats

class testProject(unittest.TestCase):

    def test_top1(self):

        result = stats.getTopCountry("Indonesia")
        self.assertEqual(result, 25610369)
