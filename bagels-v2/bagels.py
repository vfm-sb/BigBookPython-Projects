"""
Bagels -- Version 2
A Deductive Number Guessing Game.
Description:
    The secret number will be any length between 2 and 10 digits.
    Player must guess a unique-digits number based on clues.
    Player will have 10 attempts to guess the random number.
"""

# Built-in Modules
import os
import random
import string


# Functions
def generate_secret_number() -> str:
    number_of_digits = random.randint(2, 10)
    return "".join(random.sample(string.digits, number_of_digits))


def valid_guess(guess: str, digits_count: int) -> bool:
    if not guess.isdigit():
        return False
    if len(guess) != digits_count:
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


def bagels_game(lives: int = 10) -> None:
    header()
    secret_number = generate_secret_number()
    number_of_digits = len(secret_number)
    print(f"Random Number Has Been Determined and It is {number_of_digits} Digits Long!", end=" ")
    print(f"Hint: {secret_number}")
    print(f"You Have {lives} Guesses to Find The Number.")
    guess_count = 1
    while guess_count <= lives:
        print()
        print(f"Guess #{guess_count}")
        guess = input("> ")
        if guess.lower() == "force":
            break
        if guess.lower() == "hint":
            pass
        if len(guess) == number_of_digits - 1:
            guess = "0" + guess
        if not valid_guess(guess, number_of_digits):
            print("Not a Valid Guess\nGuess Again!")
            continue
        guess_count += 1
        hints = pico_fermi_bagels(secret_number, guess)
        if secret_number == guess:
            print("You Got It!")
            return
        print(" ".join(sorted(hints)))
    if guess_count == lives:
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
