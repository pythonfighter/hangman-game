import random

def choose_word():
    words = ["apple", "banana", "orange", "strawberry", "grape", "melon", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the fruit name.")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        print(display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Correct guess!")

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", word)

hangman()
