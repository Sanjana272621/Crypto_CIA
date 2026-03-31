# Route_Cipher

Route Cipher implementation using matrix transposition with hashing for integrity verification.

## Overview
This project demonstrates the Route Cipher technique, a type of transposition cipher. The message is arranged in a grid and read in a different pattern to produce the encrypted text. A simple hashing function is included to verify correctness after decryption.

## Features
- Encrypt text using Route Cipher
- Decrypt encrypted text
- Uses matrix-based transformation
- Handles padding automatically
- Includes hash-based integrity check

## How It Works

### Encryption
- Remove spaces from the message
- Fill the message row-wise into a matrix
- Read the matrix column-wise to generate cipher text
- Add padding (X) if required

Example:
HELLO WORLD → HORELLWDLXO

### Decryption
- Fill the matrix column-wise using encrypted text
- Read row-wise to get original message
- Remove padding characters

### Hashing
- Convert each character to ASCII
- Multiply by its position
- Sum all values

## Usage

Run the program:
python route_cipher.py

## Example Output

Original Message: HELLO WORLD  
Encrypted Message: HORELLWDLXO  
Decrypted Message: HELLOWORLD  
Integrity Verified

## Logic

Write: Row-wise  
Read: Column-wise  

Decryption:
Fill: Column-wise  
Read: Row-wise  

## Limitations
- Not secure for real-world encryption
- Pattern-based, can be broken with analysis

## Author
Sanjana S
