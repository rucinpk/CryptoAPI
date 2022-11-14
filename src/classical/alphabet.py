
class WhiteSpaceError(AttributeError):
    pass


class Alphabet:

    def __init__(self, alphabet: str, ignore_case: bool) -> None:
        if ignore_case:
            alphabet = alphabet.upper()

        self.character_to_index = {}
        self.index_to_character = {}
        self.length = len(alphabet)
        self.alphabet = alphabet
        self.ignore_case = ignore_case

        for i, letter in enumerate(alphabet):
            self.character_to_index[letter] = i
        for i, letter in enumerate(alphabet):
            self.index_to_character[i] = letter

    def _get_index_at_character(self, character: str) -> int:
        return self.character_to_index[character]

    def transform(self, character: str) -> str:
        if character.isspace():
            raise WhiteSpaceError("Character is whitespace")
        if self.ignore_case and character.isalpha():
            character = character.upper()
        if character not in self.character_to_index:
            raise AttributeError("Character not found in alphabet")
        return character

    def _prepare_and_get_character_index(self, character: str) -> int:
        character = self.transform(character)
        return self._get_index_at_character(character)

    def _get_character_at_index(self, index: int) -> str:
        return self.index_to_character[index % len(self)]

    def add(self, character: str, value: int) -> str:
        result_character_index = self._prepare_and_get_character_index(
            character) + value
        return self._get_character_at_index(result_character_index)

    def sub(self, character: str, value: int) -> str:
        result_character_index = self._prepare_and_get_character_index(
            character) - value
        return self._get_character_at_index(result_character_index)

    def add_letter(self, character: str, value: str) -> str:
        result_character_index = self._prepare_and_get_character_index(
            character) + self._prepare_and_get_character_index(value)
        return self._get_character_at_index(result_character_index)

    def sub_letter(self, character: str, value: str) -> str:
        result_character_index = self._prepare_and_get_character_index(
            character) - self._prepare_and_get_character_index(value)
        return self._get_character_at_index(result_character_index)

    def __len__(self):
        return self.length
