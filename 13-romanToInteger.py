import re

characters = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

combinations = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for comb in combinations.keys():
            pat = re.findall(comb, s)
            if pat:
                sum += combinations[comb]
                s = re.sub(comb, '@', s)
        for char in s:
            if char in characters.keys():
                sum += characters[char]

        return sum
