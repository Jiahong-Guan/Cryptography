class CaesarCipher:
    def __init__(self, key_shift: int):
        self.key_shift = key_shift

    def encrypt(self, plaintext: str) -> str:
        result = []

        for char in plaintext:
            if char.isalpha():
                base = 65 if char.isupper() else 97

                # Shift character base on key
                shifted_char = chr((ord(char) - base + self.key_shift) % 26 + base)
                result.append(shifted_char)
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, ciphertext: str) -> str:
        result = []

        for char in ciphertext:
            if char.isalpha():
                base = 65 if char.isupper() else 97

                # Shift character base on key
                shifted_char = chr((ord(char) - base - self.key_shift) % 26 + base)
                result.append(shifted_char)
            else:
                result.append(char)
        return ''.join(result)
