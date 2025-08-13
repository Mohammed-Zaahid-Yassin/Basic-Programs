import random

print("🎯 Welcome to the Number Guessing Game! 🎯")

# Difficulty settings
levels = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}

# Choose difficulty
while True:
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty in levels:
        attempts_left = levels[difficulty]
        break
    else:
        print("Invalid choice! Please type easy, medium, or hard.")

# Generate random number
number = random.randint(1, 100)
score = 0

print(f"\nI have picked a number between 1 and 100. You have {attempts_left} attempts!")

# Game loop
while attempts_left > 0:
    guess = input("\nEnter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts_left -= 1

    if guess < number:
        print(f"Too low! Attempts left: {attempts_left}")
    elif guess > number:
        print(f"Too high! Attempts left: {attempts_left}")
    else:
        score = attempts_left * 10  # More leftover attempts = higher score
        print(f"🎉 Correct! You guessed the number in {levels[difficulty] - attempts_left} tries.")
        print(f"Your score: {score}")
        break
else:
    print(f"❌ Out of attempts! The number was {number}. Better luck next time!")

print("\nGame Over!")
