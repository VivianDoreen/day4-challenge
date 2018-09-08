from power import power
import unittest

class TestPower(unittest.TestCase):
    def test_power_nub(self):
        result = 81
        self.assertEqual(power(3,4), result)