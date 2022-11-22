from fastapi import APIRouter
from classical.caesar import Caesar
from classical.vigenere import Vigenere
from classical.alphabet import Alphabet
from models import CaesarEncryptInput, CaesarDecryptInput, VigenereEncryptInput, VigenereDecryptInput

router = APIRouter(
    prefix="/classical",
    tags=["ciphers"]
)


@router.post("/caesar/encrypt")
async def caesar_encrypt(input: CaesarEncryptInput):
    alphabet = Alphabet(**input.alphabet.dict())

    caesar = Caesar(alphabet)
    result = caesar.encrypt(input.plaintext, input.key)

    return {"ciphertext": result}


@router.post("/caesar/decrypt")
async def caesar_decrypt(input: CaesarDecryptInput):
    alphabet = Alphabet(**input.alphabet.dict())

    caesar = Caesar(alphabet)
    result = caesar.decrypt(input.ciphertext, input.key)

    return {"plaintext": result}


@router.post("/vigenere/encrypt")
async def vigenere_encrypt(input: VigenereEncryptInput):
    alphabet = Alphabet(**input.alphabet.dict())

    vigenere = Vigenere(alphabet)
    result = vigenere.encrypt(input.plaintext, input.key)

    return {"ciphertext": result}


@router.post("/vigenere/decrypt")
async def vigenere_decrypt(input: VigenereDecryptInput):
    alphabet = Alphabet(**input.alphabet.dict())

    vigenere = Vigenere(alphabet)
    result = vigenere.decrypt(input.ciphertext, input.key)

    return {"plaintext": result}
