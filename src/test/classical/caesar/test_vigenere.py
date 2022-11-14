from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_vigenere_encrypt():

    response = client.post(
        "/classical/vigenere/encrypt",
        json={"plaintext": "attack at dawn", "key": "LEMON"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "ciphertext": "LXFOPV EF RNHR",
    }


def test_vigenere_letter_not_in_alphabet():

    response = client.post(
        "/classical/vigenere/encrypt",
        json={"plaintext": "ATTacK AT DAWN XYZ",
              "key": 3, "ignore_case": False},
    )
    assert response.status_code == 401
    assert response.json() == {
        'detail': 'Character not found'
    }
