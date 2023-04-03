"""
Bagels -- Generic Version
A Deductive Number Guessing Game.
Description:
    Player must guess a three-unique-digits number based on clues.
    Player will have 10 attempts to guess the random number.
"""

# Built-in Modules
import os
import random
import string


# Functions
def generate_secret_number() -> str:
    return "".join(random.sample(string.digits, 3))


def valid_guess(guess: str) -> bool:
    if not guess.isdigit():
        return False
    if len(guess) != 3:
        return False
    for digit in guess:
        if guess.count(digit) > 1:
            return False
    return True


def pico_fermi_bagels(secret_number: str, guess: str) -> list[str]:
    hints = []
    for index, digit in enumerate(guess):
        if digit == secret_number[index]:
            hints.append("Pico")
            continue
        if digit in list(secret_number):
            hints.append("Fermi")
    if len(hints) == 0:
        hints.append("Bagels")
    return hints


def bagels_game() -> None:
    header()
    secret_number = generate_secret_number()
    print("Random Number Has Been Determined! Hint: {}".format(secret_number))
    print("You Have 10 Guesses to Find The Number.")
    guess_count = 1
    while guess_count <= 10:
        print()
        print(f"Guess #{guess_count}")
        guess = input("> ")
        if len(guess) == 2:
            guess = "0" + guess
        if not valid_guess(guess):
            print("Not a Valid Guess\nGuess Again!")
            continue
        guess_count += 1
        hints = pico_fermi_bagels(secret_number, guess)
        if secret_number == guess:
            print("You Got It!")
            return
        print(" ".join(sorted(hints)))
    print("You Ran Out of Guesses!")
    print(f"The Number was {secret_number}")


def header():
    print(
        "Bagels, A Deductive Logic Game\n"
        f"{'-' * len('Bagels, A Deductive Logic Game')}\n"
        "Instructions:\n"
        "Pico:     If One Digit is Correct but in the Wrong Position.\n"
        "Fermi:    If One Digit is Correct and in the Right Position.\n"
        "Bagels:   If No Digits is Correct.\n"
    )


def main() -> None:
    while True:
        bagels_game()
        print("\nWould You Like To Play Again? (yes or no)")
        answer = input("> ").lower()
        if answer == "yes":
            if os.name == "posix":
                os.system("clear")
            elif os.name == "nt":
                os.system("cls")
            continue
        break
    print("Thanks For Playing!")


# Run The Game
if __name__ == "__main__":
    main()
