class BifidCipher:
    def __init__(self, key: str = "ABCDEFGHIKLMNOPQRSTUVWXYZ"):
        if not self.is_valid_key(key):
            raise ValueError("Key must contain exactly 25 unique letters (excluding 'J').")

        self.key = key.upper().replace("J", "I")
        self.polybius_square = self.create_polybius_square()

    @staticmethod
    def is_valid_key(key: str) -> bool:
        """Validate the key: must contain exactly 25 unique letters (excluding 'J')."""
        key = key.upper().replace("J", "I")
        unique_letters = set(key)

        return len(unique_letters) == 25 and all(c.isalpha() and c != 'J' for c in unique_letters)

    def create_polybius_square(self) -> dict:
        """Create the Polybius square using the given key."""
        square = {}
        index = 0

        for row in range(5):
            for col in range(5):
                square[self.key[index]] = (row, col)
                index += 1
        return square

    def encrypt(self, plaintext: str) -> str:
        plaintext = plaintext.replace(" ", "").upper()
        plaintext = plaintext.replace("J", "I")

        row_coords = []
        col_coords = []

        for char in plaintext:
            if char in self.polybius_square:
                row, col = self.polybius_square[char]
                row_coords.append(str(row))
                col_coords.append(str(col))

        combined_coords = row_coords + col_coords

        new_rows = combined_coords[::2]
        new_cols = combined_coords[1::2]

        ciphertext = ""
        for row, col in zip(new_rows, new_cols):
            row, col = int(row), int(col)

            for char, coord in self.polybius_square.items():
                if coord == (row, col):
                    ciphertext += char
                    break
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        ciphertext = ciphertext.replace(" ", "").upper()

        row_coords = []
        col_coords = []

        for char in ciphertext:
            if char in self.polybius_square:
                row, col = self.polybius_square[char]
                row_coords.append(str(row))
                col_coords.append(str(col))

        combined_coords = []
        for row, col in zip(row_coords, col_coords):
            combined_coords.append(row)
            combined_coords.append(col)

        mid = len(combined_coords) // 2
        new_rows = combined_coords[:mid]
        new_cols = combined_coords[mid:]

        plaintext = ""
        for i in range(len(new_rows)):
            row, col = int(new_rows[i]), int(new_cols[i])
            for char, coord in self.polybius_square.items():
                if coord == (row, col):
                    plaintext += char
                    break
        return plaintext
