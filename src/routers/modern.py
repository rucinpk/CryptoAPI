from fastapi import APIRouter, UploadFile, Depends, Body

from modern.xor_cipher import XorCipher
from modern.solver.xor import XorDetector, XorSolver
from models import ClassicalCipherInput, FrequencyInput
from classical.alphabet import Alphabet
from fastapi import File

router = APIRouter(
    prefix="/modern",
    tags=["modern"]
)


@router.post("/xor/encrypt")
async def xor_encrypt(text: str, key: str):
    text = text.encode()
    key = key.encode()
    initial_key = key

    key_repeated_times = len(text) // len(initial_key)

    for _ in range(key_repeated_times):
        key += initial_key

    key = key[:len(text)]

    result = XorCipher.encrypt(text, key)

    return {"data": ''.join(format(x, '02x') for x in result)}


@router.post("/xor/solve-single-xor")
async def solve_xor(input: FrequencyInput):
    alphabet = Alphabet(**input.alphabet.dict())

    xor_solver = XorSolver(alphabet)
    result = xor_solver.solve(input.text, "ENGLISH", threshold=40)

    return {"plaintext": result}


@router.post("/xor/detect-single-xor")
async def detect_xor(input: ClassicalCipherInput = Body(...), file: UploadFile = File()):
    alphabet = Alphabet(**input.alphabet.dict())

    xor_detector = XorDetector(alphabet)

    strings = (await file.read()).decode('utf-8').split("\r\n")
    result = xor_detector.detect(strings, "ENGLISH", threshold=50)

    return {"plaintext": result}


@router.post("/xor/solve-multi-xor")
async def solve_multi_key_xor(input: FrequencyInput):
    alphabet = Alphabet(**input.alphabet.dict())

    xor_solver = MultiXorSolver(alphabet)
    result = xor_solver.solve(input.text, "ENGLISH", threshold=40)

    return {"plaintext": result}
