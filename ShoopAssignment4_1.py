"""This program takes an input and decrypts it using columns."""
import math


def decrypt(encrypted, length, columns):
    message = ''
    location = 0
    row = math.ceil(length / columns)
    decrypted = []
    for _ in range(row):
        decrypted += [[' '] * columns]
    for i in range(columns):
        for j in range(row):
            if location == length:
                break
            decrypted[j][i] = encrypted[location]
            location += 1
    message = ''.join(sum(decrypted, []))
    return message


def main():
    f = open("message4.txt", "r")
    ciphertext = f.read()
    encrypted = list(ciphertext)
    length = len(ciphertext)
    for k in range(2, 13):
        print(f'\nDecrypted ({k} columns): {decrypt(encrypted, length, k)}')


if __name__ == '__main__':
    main()