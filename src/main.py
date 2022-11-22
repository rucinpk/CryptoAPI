from fastapi import FastAPI

from classical.alphabet import Alphabet
from classical.analysis.frequency import FrequencyAnalyser
from models import FrequencyInput
from routers import classical_ciphers

app = FastAPI()
app.include_router(classical_ciphers.router)


@app.post("/classical/analysis/frequency")
async def calculate_frequency(input: FrequencyInput):
    alphabet = Alphabet(**input.alphabet.dict())

    frequency_caculator = FrequencyAnalyser(alphabet)
    result = frequency_caculator.calculate(input.text)

    return {"frequencies": result}
