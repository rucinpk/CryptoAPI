from typing import Optional
from pydantic import BaseModel
from fastapi import File
import json


class AlphabetInput(BaseModel):
    letters: Optional[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ignore_case: Optional[bool] = True
    strip_whitespace: Optional[bool] = True


class ClassicalCipherInput(BaseModel):
    alphabet: Optional[AlphabetInput]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class FrequencyInput(ClassicalCipherInput):
    text: str = "Hello World!"


class FileInput(ClassicalCipherInput):
    files: bytes = File()


class ChiSquaredInput(ClassicalCipherInput):
    text: str = "Hello World!"
    language: str = "ENGLISH"


class CaesarInput(ClassicalCipherInput):
    key: int = 3


class CaesarEncryptInput(CaesarInput):
    plaintext: str = "ATTACK AT DAWN"


class CaesarDecryptInput(CaesarInput):
    ciphertext: str = "DWWDFN DW GDZQ"


class VigenereInput(ClassicalCipherInput):
    key: str = "LEMON"


class VigenereEncryptInput(VigenereInput):
    plaintext: str = "ATTACK AT DAWN"


class VigenereDecryptInput(VigenereInput):
    ciphertext: str = "LXFOPV EF RNHR"
