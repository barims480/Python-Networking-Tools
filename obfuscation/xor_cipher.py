def xor_cipher(data, key):
    """
    A simple XOR cipher for data obfuscation.
    """
    decipher = []
    num_2 = ord(key)

    for char in data:
        num = ord(char)
        result = chr(num ^ num_2)
        decipher.append(result)

    return "".join(decipher)
