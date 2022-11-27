

class XorCipher:

    @staticmethod
    def encrypt(text: bytes, key: bytes) -> bytearray:
        return bytearray([char ^ k for (char, k) in zip(text, key)])
