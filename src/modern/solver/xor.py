

from typing import List
from classical.alphabet import Alphabet
from classical.analysis.chi_squared import ChiSquaredCalculator
from modern.xor_cipher import XorCipher


class XorSolution:
    pass


class XorSolver:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def solve(self, text: str, language: str, threshold: float) -> XorSolution:
        text = bytes.fromhex(text)

        xor_cipher = XorCipher()
        chi_squared_calculator = ChiSquaredCalculator(self.alphabet)

        solutions = []

        for i in range(128):
            key = bytes(len(text) * [i])
            decrypted_text = xor_cipher.encrypt(text, key).decode()
            chi_squared = chi_squared_calculator.calculate(
                decrypted_text, language)
            solutions.append(
                (key, chi_squared, self.alphabet.preprocess(decrypted_text)))

        solutions = list(filter(lambda x: x[1] < threshold, solutions))
        seen = set()
        solutions = [
            seen.add(obj[2]) or obj for obj in solutions if obj[2] not in seen]

        return sorted(solutions, key=lambda x: x[1])


class XorDetector:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def detect(self, strings: List[str], language: str, threshold: float) -> XorSolution:
        best_results = []

        for text in strings:
            text = bytes.fromhex(text)

            xor_cipher = XorCipher()
            chi_squared_calculator = ChiSquaredCalculator(self.alphabet)

            solutions = []

            for i in range(128):
                key = bytes(len(text) * [i])
                try:
                    decrypted_text = xor_cipher.encrypt(text, key).decode()
                except UnicodeDecodeError as e:
                    continue
                chi_squared = chi_squared_calculator.calculate(
                    decrypted_text, language)
                solutions.append(
                    (key, chi_squared, self.alphabet.preprocess(decrypted_text)))

            solutions = list(filter(lambda x: x[1] < threshold, solutions))
            seen = set()
            solutions = [
                seen.add(obj[2]) or obj for obj in solutions if obj[2] not in seen]
            solutions = sorted(solutions, key=lambda x: x[1])
            best_results.extend(solutions)
        return sorted(best_results, key=lambda x: x[1])
