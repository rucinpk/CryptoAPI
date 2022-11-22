
class WhiteSpaceError(AttributeError):
    pass


class Alphabet:

    def __init__(self, letters: str, ignore_case: bool, strip_whitespace) -> None:
        if ignore_case:
            alphabet = letters.upper()

        self.character_to_index = {}
        self.index_to_character = {}
        self.length = len(alphabet)
        self.alphabet = alphabet
        self.ignore_case = ignore_case
        self.strip_whitespace = strip_whitespace

        for i, letter in enumerate(alphabet):
            self.character_to_index[letter] = i
        for i, letter in enumerate(alphabet):
            self.index_to_character[i] = letter

        self._current = 0

    def _get_index_at_character(self, character: str) -> int:
        return self.character_to_index[character]

    def preprocess(self, text: str) -> str:
        if self.strip_whitespace:
            text = "".join(
                list(filter(lambda character: not character.isspace(), text)))
        if self.ignore_case:
            text = "".join(
                list(map(lambda character: character.upper(), text)))
        text = "".join(list(
            filter(lambda character: character in self.character_to_index, text)))

        return text

    def strip(self, text: str) -> str:
        return "".join(list(filter(lambda letter: letter in self.alphabet, text)))

    def _get_character_at_index(self, index: int) -> str:
        return self.index_to_character[index % len(self)]

    def add(self, character: str, value: int) -> str:
        index = self._get_index_at_character(character)
        result_character_index = index + value
        return self._get_character_at_index(result_character_index)

    def sub(self, character: str, value: int) -> str:
        index = self._get_index_at_character(character)
        result_character_index = index - value
        return self._get_character_at_index(result_character_index)

    def add_letter(self, character: str, value: str) -> str:
        left = self._get_index_at_character(character)
        value = self.preprocess(value)
        right = self._get_index_at_character(value)
        result_character_index = left + right
        return self._get_character_at_index(result_character_index)

    def sub_letter(self, character: str, value: str) -> str:
        left = self._get_index_at_character(character)
        value = self.preprocess(value)
        right = self._get_index_at_character(value)
        result_character_index = left - right
        return self._get_character_at_index(result_character_index)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self._current += 1
        if self._current < len(self):
            return self.alphabet[self._current - 1]
        self._current = 0
        raise StopIteration
