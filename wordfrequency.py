# Word Frequency Counter

from collections import Counter

# Get text from user
text = input("Enter a paragraph of text:\n")

# Normalize case, remove punctuation, and split into words
words = text.lower().split()

# Count word occurrences
word_counts = Counter(words)

# Display results sorted by frequency
print("\nWord Frequencies:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}")
