from typing import Dict

from classical.alphabet import Alphabet


class FrequencyAnalyser:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def calculate(self, text: str) -> Dict[str, int]:
        text = self.alphabet.preprocess(text)

        letter_sums = {}

        total_letters = 0

        for letter in text:
            if letter in letter_sums:
                letter_sums[letter] += 1
            else:
                letter_sums[letter] = 1
            total_letters += 1
        frequencies = {}

        for letter, letter_count in letter_sums.items():
            frequencies[letter] = float(letter_count) / total_letters

        return frequencies


class GermanFrequency:

    def get(self):
        {
            "A":	5.58,
            "Ä":	0.54,
            "B":	1.96,
            "C":	3.16,
            "D":	4.98,
            "E":	16.93,
            "F":	1.49,
            "G":	3.02,
            "H":	4.98,
            "I":	8.02,
            "J":	0.24,
            "K":	1.32,
            "L":	3.60,
            "M":	2.55,
            "N":	10.53,
            "O":	2.24,
            "Ö":	0.30,
            "P":	0.67,
            "Q":	0.02,
            "R":	6.89,
            "ß":	0.37,
            "S":	6.42,
            "T":	5.79,
            "U":	3.83,
            "Ü":	0.65,
            "V":	0.84,
            "W":	1.78,
            "X":	0.05,
            "Y":	0.05,
            "Z":	1.21,
        }


class EnglishFrequency:
    def get(self):
        {
            "E":	12.02,
            "T":	9.10,
            "A":	8.12,
            "O":	7.68,
            "I":	7.31,
            "N":	6.95,
            "S":	6.28,
            "R":	6.02,
            "H":	5.92,
            "D":	4.32,
            "L":	3.98,
            "U":	2.88,
            "C":	2.71,
            "M":	2.61,
            "F":	2.30,
            "Y":	2.11,
            "W":	2.09,
            "G":	2.03,
            "P":	1.82,
            "B":	1.49,
            "V":	1.11,
            "K":	0.69,
            "X":	0.17,
            "Q":	0.11,
            "J":	0.10,
            "Z":	0.07,
        }
