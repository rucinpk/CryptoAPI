
from typing import Dict

from classical.alphabet import Alphabet


class CoincidenceCalculator:
    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet
