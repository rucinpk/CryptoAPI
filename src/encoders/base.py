import base64


class Base64Encoder:

    @staticmethod
    def encode(text: str) -> str:
        return base64.encode(text)

    @staticmethod
    def decode(text: str) -> str:
        return base64.decode(text)
