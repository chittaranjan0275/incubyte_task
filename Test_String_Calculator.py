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
        """this should add multiple numbers in string"""
        self.assertEqual(StringCalculator.add('1,2,3'), 6)

    def test_sum_of_alpha(self):
        """this should return sum for alphabet answer numbers in string"""
        self.assertEqual(StringCalculator.add('1,2,a,c'), 7)

    def test_negative_numbers_exception(self):
        """raise exception for negative numbers"""
        self.assertRaises(Exception, StringCalculator.add, '-1,-2,-3,1,2,3')

    def test_ignore_greater_than_1000(self):
        """this should ignore numbers greater than 1000"""
        self.assertEqual(StringCalculator.add('2, 1001'), 2)

    def test_new_line_delimiters_as_a_comma(self):
        """this should use new line delimiter as comma"""
        self.assertEqual(StringCalculator.add('1\n2,3'), 6)

    def test_support_different_delimiters(self):
        """this should use different delimiters"""
        self.assertEqual(StringCalculator.add('//;\n1;2'), 3)

    def test_any_length_delimiters(self):
        """this should any lenght of delimiters"""
        self.assertEqual(StringCalculator.add('//[***]\n1***2***3'), 6)
