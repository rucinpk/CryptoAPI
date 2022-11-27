from fastapi import APIRouter

from encoders.base import Base64Encoder

router = APIRouter(
    prefix="/encoders",
    tags=["encoders"]
)


@router.post("/base64/encode")
async def base64_encode(text: str):
    return {"data": Base64Encoder.encode(text)}


@router.post("/base64/decode")
async def base64_encode(text: str):
    return {"data": Base64Encoder.decode(text)}
