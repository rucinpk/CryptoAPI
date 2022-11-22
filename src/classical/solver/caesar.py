

from classical.alphabet import Alphabet
from classical.analysis.chi_squared import ChiSquaredCalculator
from classical.caesar import Caesar


class CaesarSolution:
    pass


class CaesarSolver:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def solve(self, text: str, language: str) -> CaesarSolution:
        text = self.alphabet.preprocess(text)
        caesar_cipher = Caesar(self.alphabet)
        chi_squared_calculator = ChiSquaredCalculator(self.alphabet)

        solutions = []

        for i in range(len(self.alphabet)):
            decrypted_text = caesar_cipher.decrypt(text, i)
            chi_squared = chi_squared_calculator.calculate(
                decrypted_text, language)
            solutions.append((i, chi_squared, decrypted_text))

        return sorted(solutions, key=lambda x: x[1])
