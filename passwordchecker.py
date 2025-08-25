import re
def password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    symbol_criteria = re.search(r"[^A-Za-z0-9]", password) is not None

    score = sum([length_criteria, digit_criteria, upper_criteria, lower_criteria, symbol_criteria])

    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter a password to check its strength: ")
result = password_strength(password)
print(f"Password strength: {result}")
