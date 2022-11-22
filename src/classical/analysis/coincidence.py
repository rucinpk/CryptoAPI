import collections

from classical.alphabet import Alphabet


class CoincidenceCalculator:
    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def calculate(self, text: str) -> None:
        text = self.alphabet.preprocess(text)
        num_chars = len(text)
        freqs = collections.Counter(text)
        frequency_sum = 0.0

        for letter in self.alphabet:
            frequency_sum += freqs[letter] * (freqs[letter] - 1)

        return frequency_sum / (num_chars * (num_chars - 1))
