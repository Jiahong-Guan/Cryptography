class AtbashCipher:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.reversed_alphabet = self.alphabet[::-1]

        self.translation_table = str.maketrans(
            self.alphabet + self.alphabet.lower(),
            self.reversed_alphabet + self.reversed_alphabet.lower()
        )

    def transform(self, text: str) -> str:
        return text.translate(self.translation_table)
