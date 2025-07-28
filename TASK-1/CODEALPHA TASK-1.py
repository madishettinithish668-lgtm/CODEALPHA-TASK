import random

# Predefined words
words = ["python", "hangman", "code", "random", "guess"]
word = random.choice(words)

# Game setup
guessed = []
tries = 6
display = ["_" for _ in word]

print("HANGMAN GAME")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect attempts. Good luck!\n")

# Game loop
while tries > 0 and "_" in display:
    print("------------------------------------------------")
    print("Word:", " ".join(display))
    print(f"Tries Left: {tries}")
    print(f"Letters Guessed: {' '.join(guessed) if guessed else 'None'}")

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single alphabet.")
        continue

    if guess in guessed:
        print("Already guessed! Try a new letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Nice! Letter found.")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess.")
        tries -= 1

# Final result
print("------------------------------------------------")
if "_" not in display:
    print("Congratulations! You guessed the word:", word.upper())
else:
    print("Game Over! The correct word was:", word.upper())
