import random

print("----welcome to user-------")
print("----starting game-------")
name = input("-----Hangman Game ------\nplease enter your name: ")
print(f"----welcome {name} to the start of the game-------")

# Word lists for each difficulty
easy_words = ["banana", "apple", "grape", "orange", "mango", 
              "peach", "kiwi", "pear", "plum", "melon"]

medium_words = ["tiger", "elephant", "giraffe", "kangaroo", "panda", 
                "zebra", "lion", "rabbit", "monkey", "camel"]

hard_words = ["australia", "bangladesh", "switzerland", "philippines", "venezuela", 
              "kazakhstan", "madagascar", "netherlands", "singapore", "argentina"]

# Difficulty selection
print("\nChoose difficulty level:")
print("1. Easy (10 attempts, fruits)")
print("2. Medium (7 attempts, animals)")
print("3. Hard (5 attempts, countries)")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    attempts = 10
    words = easy_words
elif choice == "2":
    attempts = 7
    words = medium_words
elif choice == "3":
    attempts = 5
    words = hard_words
else:
    print("Invalid choice! Defaulting to Medium difficulty.")
    attempts = 7
    words = medium_words

# Select random word from chosen list
word = random.choice(words).lower()
guessed = ["_"] * len(word)
guessed_letters = []

print("\nWelcome to the simple hangman game!")
print("--Guess the word by entering one letter at a time--")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter to guess: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input! Please enter a single letter.")
        continue

    # Already guessed check
    if guess in guessed_letters:
        print(f"You have already guessed the letter '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("\nGood job!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("\nSorry, wrong guess!")
        attempts -= 1
        print(f"You have {attempts} attempts left.")

    print(" ".join(guessed))

# Win/Lose condition
if "_" not in guessed:
    print(f"\n🎉 Congratulations {name}! You guessed the word '{word}' correctly!")
else:
    print(f"\n💀 Game Over {name}! The word was '{word}'.")
