from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_caesar_encrypt():

    response = client.post(
        "/classical/caesar/encrypt",
        json={"plaintext": "ATTACK AT DAWN XYZ", "key": 3},
    )
    assert response.status_code == 200
    assert response.json() == {
        "ciphertext": "DWWDFN DW GDZQ ABC",
    }


def test_caesar_letter_not_in_alphabet():

    response = client.post(
        "/classical/caesar/encrypt",
        json={"plaintext": "ATTacK AT DAWN XYZ",
              "key": 3, "ignore_case": False},
    )
    assert response.status_code == 401
    assert response.json() == {
        'detail': 'Character not found'
    }
