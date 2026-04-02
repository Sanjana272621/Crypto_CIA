# Route Cipher and Custom Hash Implementation

## 1. Overview

This project implements:

1. A Route Cipher for encryption and decryption
2. A custom hashing function implemented from scratch
3. A test script showing the complete encrypt, hash and decrypt round-trip

## 2. Theory Behind the Route Cipher

A Route Cipher is a type of transposition cipher. In a transposition cipher, the original characters of the plaintext are not changed, but their positions are rearranged according to a fixed rule.

In this implementation:

- The plaintext is first converted to uppercase
- Only alphanumeric characters are kept
- The cleaned plaintext is written into a rectangular grid row by row
- The ciphertext is produced by reading the grid in clockwise spiral order

### Encryption steps

1. Prepare the plaintext by removing spaces and punctuation and converting to uppercase
2. Choose the number of columns as the key
3. Compute the required number of rows
4. Pad the plaintext with `X` if necessary
5. Fill the grid row-wise
6. Read the characters in clockwise spiral order

### Decryption steps

1. Create an empty grid of the same size
2. Fill the ciphertext into the grid in clockwise spiral order
3. Read the grid row-wise
4. Remove trailing padding `X`

## 3. Theory Behind the Hash Function

This project uses a custom bitwise hash function designed using shift and XOR operations.

Unlike traditional arithmetic-based hashes (such as polynomial rolling hash), this implementation uses low-level bit manipulation to combine character values.

For each character in the text:

1. The current hash is left-shifted by 5 bits and added to itself:
   (h << 5) + h  
   This is equivalent to multiplying the hash by 33.

2. The result is then XORed with the ASCII value of the character along with its position index:
   h = ((h << 5) + h) ^ (ASCII value + position)

3. Additional mixing is performed using a right shift:
   h = h ^ (h >> 7)

4. Finally, the hash is constrained to 32 bits:
   h = h & 0xFFFFFFFF

This combination of shifting and XOR operations ensures that:
- The order of characters affects the hash
- Each character contributes differently based on its position
- Small changes in input produce different hash outputs


## 4. Justification for the Chosen Hash

I chose a custom bitwise hash function because:

- Avoids standard polynomial hashing patterns
- Uses bit manipulation to mix input data efficiently
- Small changes in input produce different hash outputs
- Produces position-sensitive and order-dependent hash values


## 5. How to Run

Make sure Python 3 is installed.

Run:

```bash
python test_roundtrip.py
```