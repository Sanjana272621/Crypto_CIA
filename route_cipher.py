import math

PADDING_CHAR = 'X'

#Convert to uppercase and keep alphanumeric only
def prepare_text(text):
    cleaned = []
    for ch in text.upper():
        if ch.isalnum():
            cleaned.append(ch)
    return ''.join(cleaned)

#Return a list of (row, col) positions in clockwise spiral order
def spiral_order_positions(rows, cols):
    
    positions = []

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            positions.append((top, c))
        top += 1

        for r in range(top, bottom + 1):
            positions.append((r, right))
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                positions.append((bottom, c))
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                positions.append((r, left))
            left += 1

    return positions


def create_grid_rowwise(text, rows, cols):
    grid = []
    index = 0

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(text[index])
            index += 1
        grid.append(row)

    return grid


def encrypt_route_cipher(plaintext, cols):
    plaintext = prepare_text(plaintext)

    if cols <= 0:
        raise ValueError("Number of columns must be greater than 0.")

    if len(plaintext) == 0:
        return ""

    rows = math.ceil(len(plaintext) / cols)
    total_cells = rows * cols

    padded_plaintext = plaintext + PADDING_CHAR * (total_cells - len(plaintext))
    grid = create_grid_rowwise(padded_plaintext, rows, cols)
    positions = spiral_order_positions(rows, cols)

    ciphertext = ''.join(grid[r][c] for r, c in positions)
    return ciphertext


def decrypt_route_cipher(ciphertext, cols):
    if cols <= 0:
        raise ValueError("Number of columns must be greater than 0.")

    if len(ciphertext) == 0:
        return ""

    rows = math.ceil(len(ciphertext) / cols)

    if rows * cols != len(ciphertext):
        raise ValueError("Invalid ciphertext length for the given number of columns.")

    grid = [['' for _ in range(cols)] for _ in range(rows)]
    positions = spiral_order_positions(rows, cols)

    index = 0
    for r, c in positions:
        grid[r][c] = ciphertext[index]
        index += 1

    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext.rstrip(PADDING_CHAR)


if __name__ == "__main__":
    sample_text = "HELLO WORLD"
    key_cols = 4

    encrypted = encrypt_route_cipher(sample_text, key_cols)
    decrypted = decrypt_route_cipher(encrypted, key_cols)

    print("Sample plaintext :", sample_text)
    print("Encrypted        :", encrypted)
    print("Decrypted        :", decrypted)