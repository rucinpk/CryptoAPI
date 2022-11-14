from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from classical.alphabet import Alphabet
from classical.caesar import Caesar
from classical.vigenere import Vigenere
from classical.analysis.frequency import FrequencyAnalyser

app = FastAPI()


class ClassicalCipherInput(BaseModel):
    alphabet: Optional[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ignore_case: Optional[bool] = True


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


class FrequencyInput(BaseModel):
    alphabet: Optional[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text: str = "Hello World!"
    ignore_case: Optional[bool] = True


@app.post("/classical/caesar/encrypt")
async def caesar_encrypt(input: CaesarEncryptInput):
    alphabet = Alphabet(input.alphabet, input.ignore_case)

    caesar = Caesar(alphabet)
    result = caesar.encrypt(input.plaintext, input.key)

    return {"ciphertext": result}


@app.post("/classical/caesar/decrypt")
async def caesar_decrypt(input: CaesarDecryptInput):
    alphabet = Alphabet(input.alphabet, input.ignore_case)

    caesar = Caesar(alphabet)
    result = caesar.decrypt(input.ciphertext, input.key)

    return {"plaintext": result}


@app.post("/classical/vigenere/encrypt")
async def vigenere_encrypt(input: VigenereEncryptInput):
    alphabet = Alphabet(input.alphabet, input.ignore_case)

    vigenere = Vigenere(alphabet)
    result = vigenere.encrypt(input.plaintext, input.key)

    return {"ciphertext": result}


@app.post("/classical/vigenere/decrypt")
async def vigenere_decrypt(input: VigenereDecryptInput):
    alphabet = Alphabet(input.alphabet, input.ignore_case)

    vigenere = Vigenere(alphabet)
    result = vigenere.decrypt(input.ciphertext, input.key)

    return {"plaintext": result}


@app.post("/classical/analysis/frequency")
async def calculate_frequency(input: FrequencyInput):
    alphabet = Alphabet(input.alphabet, input.ignore_case)

    frequency_caculator = FrequencyAnalyser(alphabet)
    result = frequency_caculator.calculate(input.text)

    return {"frequencies": result}
