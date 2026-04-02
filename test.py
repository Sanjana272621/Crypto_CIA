from route_cipher import encrypt_route_cipher, decrypt_route_cipher, prepare_text
from custom_hash import bitwise_hash, bitwise_hash_hex


def run_test(plaintext, cols):
    processed_plaintext = prepare_text(plaintext)
    ciphertext = encrypt_route_cipher(plaintext, cols)
    recovered_plaintext = decrypt_route_cipher(ciphertext, cols)
    hash_value_int = bitwise_hash(ciphertext)
    hash_value_hex = bitwise_hash_hex(ciphertext)

    print("Original plaintext: ", plaintext)
    print("Processed plaintext: ", processed_plaintext)
    print("Key (columns): ", cols)
    print("Ciphertext: ", ciphertext)
    print("Hash (integer): ", hash_value_int)
    print("Hash (hex): ", hash_value_hex)
    print("Decrypted plaintext: ", recovered_plaintext)
    print("Success: ", recovered_plaintext == processed_plaintext)


if __name__ == "__main__":
    run_test("HELLO WORLD", 4)