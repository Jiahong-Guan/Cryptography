class ColumnarTranspositionCipher:
    def __init__(self, keyword: str):
        self.keyword = keyword.strip()
        self.keyword_order = self.create_keyword_order()

    def create_keyword_order(self):
        return sorted(range(len(self.keyword)), key=lambda x: self.keyword[x])

    def encrypt(self, plaintext: str) -> str:
        plaintext = plaintext.replace(" ", "").strip()

        num_cols = len(self.keyword)
        num_rows = len(plaintext) // num_cols + (1 if len(plaintext) % num_cols != 0 else 0)

        grid = ['' for _ in range(num_rows)]
        index = 0

        # Fill the grid row by row
        for row in range(num_rows):
            for col in range(num_cols):
                if index < len(plaintext):
                    grid[row] += plaintext[index]
                    index += 1

        # Rearrange columns to form ciphertext
        ciphertext = ''
        for col in self.keyword_order:
            for row in range(num_rows):
                if col < len(grid[row]):
                    ciphertext += grid[row][col]

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        num_cols = len(self.keyword)
        num_rows = len(ciphertext) // num_cols

        columns = [ciphertext[i:i+num_rows] for i in range(0, len(ciphertext), num_rows)]

        sorted_columns = [''] * num_cols
        for i, col in zip(self.keyword_order, columns):
            sorted_columns[i] = col

        # Rearrange row to form plaintext
        plaintext = ''
        for row in range(num_rows):
            for col in range(num_cols):
                if row < len(sorted_columns[col]):
                    plaintext += sorted_columns[col][row]

        return plaintext
