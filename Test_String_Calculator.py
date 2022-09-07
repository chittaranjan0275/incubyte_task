import unittest

from String_Calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        """this should return 0 if string is empty"""
        self.assertEqual(StringCalculator.add(''), 0)

    def test_add_single_string(self):
        """this should return string as it is"""
        self.assertEqual(StringCalculator.add('1'), 1)

    def test_add_two_strings(self):
        """this should add 2 numbers in string seperated by comma"""
        self.assertEqual(StringCalculator.add('1,2'), 3)

    def test_add_multiple_string(self):
        self.assertEqual(StringCalculator.add('1,2,3'), 6)

    def test_ignore_greater_than_1000(self):
        self.assertEqual(StringCalculator.add('2, 1001'), 2)
