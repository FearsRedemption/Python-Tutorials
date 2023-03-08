import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# ENCRYPTION
plainText = input("Enter your message to encrypt: ")
cipherText = ""

for letter in plainText:
    cipherText += key[chars.index(letter)]

print(f"Original: {plainText}")
print(f"Encrypted: {cipherText}")

# DECRYPT
cipherText = input("Enter your message to decrypt: ")
plainText = ""

for letter in cipherText:
    plainText += chars[key.index(letter)]

print(f"Encrypted: {cipherText}")
print(f"Original: {plainText}")

