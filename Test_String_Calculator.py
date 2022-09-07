import unittest

from String_Calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        """this should return 0 if string is empty"""
        self.assertEqual(StringCalculator.add(''), 0)
