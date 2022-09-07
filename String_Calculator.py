import re


class StringCalculator():

    def add(Number):
        if Number == '':
            return 0
        Number = map(int, re.findall(r"-?\d+", Number))
        return sum(Number)