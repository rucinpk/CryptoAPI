from classical.alphabet import Alphabet


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
        return "".join([transform_func(letter, expanded_key[i])
                        for i, letter in enumerate(plaintext)])

    def encrypt(self, plaintext: str, key: str) -> str:
        return self._vigenere_core(plaintext, key, self.alphabet.add_letter)

    def decrypt(self, plaintext: str, key: str) -> str:
        return self._vigenere_core(plaintext, key, self.alphabet.sub_letter)
