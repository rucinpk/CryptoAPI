from fastapi import FastAPI

from classical.alphabet import Alphabet
from classical.analysis.frequency import FrequencyAnalyser
from classical.analysis.coincidence import CoincidenceCalculator
from models import ChiSquaredInput, FrequencyInput
from routers import classical_ciphers
from classical.analysis.chi_squared import ChiSquaredCalculator

app = FastAPI()
app.include_router(classical_ciphers.router)


@app.post("/classical/analysis/frequency")
async def calculate_frequency(input: FrequencyInput):
    alphabet = Alphabet(**input.alphabet.dict())

    frequency_caculator = FrequencyAnalyser(alphabet)
    result = frequency_caculator.calculate(input.text)

    return {"frequencies": result}


@app.post("/classical/analysis/index-of-coincidence")
async def calculate_ioc(input: FrequencyInput):
    alphabet = Alphabet(**input.alphabet.dict())

    coincidence_calculator = CoincidenceCalculator(alphabet)
    result = coincidence_calculator.calculate(input.text)

    return {"indexOfCoincidence": result}


@app.post("/classical/analysis/chi-squared")
async def calculate_chi_squared(input: ChiSquaredInput):
    alphabet = Alphabet(**input.alphabet.dict())

    chi_squared_calculator = ChiSquaredCalculator(alphabet)
    result = chi_squared_calculator.calculate(input.text, input.language)

    return {"chiSquared": result}
