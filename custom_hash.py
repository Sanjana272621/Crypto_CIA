def bitwise_hash(text):
    h = 5381  

    for i, ch in enumerate(text):
        char_val = ord(ch)

        # Core mixing
        h = ((h << 5) + h) ^ (char_val + i)

        h = h ^ (h >> 7)

        #Keep it bounded
        h = h & 0xFFFFFFFF  #32-bit constraint

    return h


def bitwise_hash_hex(text):
    return hex(bitwise_hash(text))


if __name__ == "__main__":
    sample = "HELLOWORLD"
    print("Text       :", sample)
    print("Hash (int) :", bitwise_hash(sample))
    print("Hash (hex) :", bitwise_hash_hex(sample))