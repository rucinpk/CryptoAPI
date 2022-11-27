from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_caesar_encrypt():

    response = client.post(
        "/encoders/base64/encode",
        json={"text": "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",
    }
