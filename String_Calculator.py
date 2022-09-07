import re


class StringCalculator:

    def add(numbers):
        dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                'x': 24, 'y': 25, 'z': 26, }
        sum_of_alpha = 0

        """calculate sum of alphabet in strings"""
        for x in numbers:
            if x.isalpha() == True:
                sum_of_alpha += dict[x]
        if numbers == '':
            return 0
        numbers = map(int, re.findall(r"-?\d+", numbers))

        """"remove numbers less than 1000 from string"""
        numbers = list(filter(lambda x: x < 1000, numbers))

        """inline function to filter negative numbers"""
        negative_numbers = list(filter(lambda x: x < 0, numbers))

        if negative_numbers:
            """raise exception for negative numbers"""
            raise Exception('negatives not allowed ' + negative_numbers)

        """return sum of string having numbers and alphabet"""
        return sum(numbers) + sum_of_alpha
