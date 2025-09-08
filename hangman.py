import random

words = ["python", "hardware", "laptop", "science", "project", "security", "formula", "engineer"]
word = random.choice(words)
guessed = set()
attempts_left = 7

print("Welcome to Hangman!")
display = ['_' if c.isalpha() else c for c in word]

while attempts_left > 0 and '_' in display:
    print("\nWord:", ' '.join(display))
    print(f"Guessed letters: {', '.join(sorted(guessed))}" if guessed else "No letters guessed yet.")
    print(f"Attempts left: {attempts_left}")
    guess = input("Guess a letter: ").lower()
    if not (guess.isalpha() and len(guess) == 1):
        print("Please guess a single alphabet letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    guessed.add(guess)
    if guess in word:
        print("Good guess!")
        for idx, c in enumerate(word):
            if c == guess:
                display[idx] = guess
    else:
        print("Wrong guess!")
        attempts_left -= 1

if '_' not in display:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame over! The word was: {word}")
