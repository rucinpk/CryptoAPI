from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_caesar_encrypt():

    response = client.post(
        "/modern/xor/encrypt",
        json={"text": "1c0111001f010100061a024b53535009181c",
              "key": "686974207468652062756c6c277320657965"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": "746865206b696420646f6e277420706c6179",
    }
