from collections import Counter
from typing import Dict

from classical.alphabet import Alphabet
from classical.analysis.frequency import FREQUENCIES, FrequencyAnalyser


class ChiSquaredCalculator:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def calculate(self, text: str, language: str) -> float:
        text = self.alphabet.preprocess(text)

        freqs = Counter(text)

        for letter in self.alphabet:
            if letter not in freqs:
                freqs[letter] = 0.0

        expected_frequencies = self._calculate_expected_occurences(
            FREQUENCIES[language], len(text))

        chi_sum = 0.0
        for letter in self.alphabet:
            square = pow(freqs[letter] - expected_frequencies[letter], 2)
            chi_sum += square / expected_frequencies[letter]

        return chi_sum

    def _calculate_expected_occurences(self, language_frequencies, text_length) -> Dict[str, float]:
        expected_occurences = {}
        for letter in self.alphabet:
            expected_occurences[letter] = (
                language_frequencies[letter] / 100) * text_length

        return expected_occurences
