
from fastapi import HTTPException

from classical.alphabet import Alphabet, WhiteSpaceError


class Caesar:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def _caesar_core(self, plaintext, key, transform_func):
        result = []
        for letter in plaintext:
            try:
                encrypted = transform_func(letter, key)
            except WhiteSpaceError as e:
                encrypted = letter
            except AttributeError as e:
                raise HTTPException(
                    status_code=400, detail="Character not found") from e
            result.append(encrypted)
        return "".join(result)

    def encrypt(self, plaintext: str, key: int) -> str:
        return self._caesar_core(plaintext, key, self.alphabet.add)

    def decrypt(self, plaintext: str, key: int) -> str:
        return self._caesar_core(plaintext, key, self.alphabet.sub)
