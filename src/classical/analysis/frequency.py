from typing import Dict

from fastapi import HTTPException

from classical.alphabet import Alphabet, WhiteSpaceError


class FrequencyAnalyser:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def calculate(self, text: str) -> Dict[str, int]:
        letter_sums = {}

        total_letters = 0

        for letter in text:
            try:
                transformed_letter = self.alphabet.transform(letter)
            except WhiteSpaceError as e:
                transformed_letter = letter
            except AttributeError as e:
                raise HTTPException(
                    status_code=400, detail="Character not found") from e
            if transformed_letter in letter_sums:
                letter_sums[transformed_letter] += 1
            else:
                letter_sums[transformed_letter] = 1
            total_letters += 1
        frequencies = {}

        for letter, letter_count in letter_sums.items():
            frequencies[letter] = float(letter_count) / total_letters

        return frequencies
