def reverse_cipher(text):
    return text[::-1]
msg = input("Enter the message to encrypt: ")
encrypted = reverse_cipher(msg)
print("Encrypted message:", encrypted)
decrypted = reverse_cipher(encrypted)
print("Decrypted message:", decrypted)
