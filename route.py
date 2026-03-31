# Implementing Route Cypher
def encrypt_route_cipher(message, rows):
    message = message.replace(" ", "")  # remove spaces
    cols = len(message) // rows

    # Add padding if needed
    if len(message) % rows != 0:
        cols += 1
        message += 'X' * (rows * cols - len(message))

    # Create matrix
    matrix = []
    index = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(message[index])
            index += 1
        matrix.append(row)

    # Read column-wise
    encrypted = ""
    for c in range(cols):
        for r in range(rows):
            encrypted += matrix[r][c]

    return encrypted


# Route Cypher Decrypton
def decrypt_route_cipher(cipher, rows):
    cols = len(cipher) // rows

    # Create empty matrix
    matrix = [[None for _ in range(cols)] for _ in range(rows)]

    index = 0

    # Fill column-wise
    for c in range(cols):
        for r in range(rows):
            matrix[r][c] = cipher[index]
            index += 1

    # Read row-wise
    decrypted = ""
    for r in range(rows):
        for c in range(cols):
            decrypted += matrix[r][c]

    return decrypted.rstrip('X')  # remove padding

# Simple Hash Function
def simple_hash(text):
    hash_value = 0
    for i, char in enumerate(text):
        hash_value += (i + 1) * ord(char)
    return hash_value

if __name__ == "__main__":
    message = "HELLO WORLD"
    rows = 3

    print("Original:", message)

    # Normalize original message for hashing
    normalized_message = message.replace(" ", "").upper()

    # Encrypt
    encrypted = encrypt_route_cipher(message, rows)
    print("Encrypted:", encrypted)

    # Hash original (normalized)
    original_hash = simple_hash(normalized_message)
    print("Original Hash:", original_hash)

    # Decrypt
    decrypted = decrypt_route_cipher(encrypted, rows)
    print("Decrypted:", decrypted)

    # Hash decrypted
    decrypted_hash = simple_hash(decrypted)
    print("Decrypted Hash:", decrypted_hash)

    # Verify integrity
    if original_hash == decrypted_hash:
        print("Integrity Verified")
    else:
        print("Integrity Failed")
