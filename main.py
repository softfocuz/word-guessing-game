import random

category = "fruit"

def word_guessing_game():
    words = ["orange", "apple", "durian", "banana", "grapes", "peach", "watermelon", "papaya",
             "guava", "cherry", "strawberry", "pineapple", "lemon", "plum"]
    hidden_word = random.choice(words)

    guessed_letters = []
    attempts = 6

    print("Guess the word letter by letter.")
    print(f"Category: {category}")

    while attempts > 0:
        display_word = ""

        for letter in hidden_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        if "_" not in display_word:
            print("You won! The word was:", hidden_word)
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in hidden_word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if attempts == 0:
        print("Game Over! The word was:", hidden_word)

word_guessing_game()