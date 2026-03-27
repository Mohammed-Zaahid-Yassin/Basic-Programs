import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not chars:
        return "No character set selected!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_upper, use_digits, use_symbols)
print("Generated password:", password)
