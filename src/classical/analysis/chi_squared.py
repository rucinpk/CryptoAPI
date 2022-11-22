from typing import Dict
import collections

from classical.alphabet import Alphabet
from classical.analysis.frequency import FREQUENCIES, FrequencyAnalyser

CHI_SQUARED_STATISTICS = {
    "ENGLISH": "ASD"
}


class ChiSquaredCalculator:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def calculate(self, text: str, language: str) -> Dict[str, int]:
        text = self.alphabet.preprocess(text)

        freq_analyser = FrequencyAnalyser(self.alphabet)
        freqs = freq_analyser.calculate(text)

        for letter in self.alphabet:
            if letter not in freqs:
                freqs[letter] = 0.0

        expected_frequencies = self._calculate_expected_occurences(
            FREQUENCIES[language], len(text))

        chi_sum = 0.0
        for letter in self.alphabet:
            chi_sum += ((freqs[letter] - expected_frequencies[letter])
                        ** 2) / expected_frequencies[letter]

        return chi_sum

    def _calculate_expected_occurences(self, language_frequencies, text_length) -> Dict[str, float]:
        expected_occurences = {}
        for letter in self.alphabet:
            expected_occurences[letter] = (
                language_frequencies[letter] / 100) * text_length
        return expected_occurences
