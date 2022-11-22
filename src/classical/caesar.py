from classical.alphabet import Alphabet


class Caesar:

    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet

    def _caesar_core(self, text, key, transform_func):
        text = self.alphabet.preprocess(text)
        result = list(
            map(lambda letter: transform_func(letter, key), text))
        return "".join(result)

    def encrypt(self, plaintext: str, key: int) -> str:
        return self._caesar_core(plaintext, key, self.alphabet.add)

    def decrypt(self, plaintext: str, key: int) -> str:
        return self._caesar_core(plaintext, key, self.alphabet.sub)
