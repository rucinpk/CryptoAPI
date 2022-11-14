
from fastapi import HTTPException

from classical.alphabet import Alphabet, WhiteSpaceError


class Vigenere:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def _expand_key(self, plaintext, key):
        result_key = []

        key_iterator = 0
        for character in plaintext:
            if character.isspace():
                result_key.append(character)
            else:
                result_key.append(key[key_iterator % len(key)])
                key_iterator += 1
        return "".join(result_key)

    def _vigenere_core(self, plaintext, key, transform_func):
        expanded_key = self._expand_key(plaintext, key)

        result = []
        for i, letter in enumerate(plaintext):
            try:
                encrypted = transform_func(letter, expanded_key[i])
            except WhiteSpaceError as e:
                encrypted = letter
            except AttributeError as e:
                raise HTTPException(
                    status_code=400, detail="Character not found") from e
            result.append(encrypted)
        return "".join(result)

    def encrypt(self, plaintext: str, key: str) -> str:
        return self._vigenere_core(plaintext, key, self.alphabet.add_letter)

    def decrypt(self, plaintext: str, key: str) -> str:
        return self._vigenere_core(plaintext, key, self.alphabet.sub_letter)
