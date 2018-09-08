from sum_lists import sum1
import unittest

class TestSumLists(unittest.TestCase):
    def test_sum(self):
        result = 40
        self.assertEqual(sum1([4, 5, [1,2], 8, 4, [8, 3, 5]]), result)