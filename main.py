from random import randint
from time import sleep

# Define ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

def no_of_chances(choice):
    chances_dict = {"1": 10, "2": 5, "3": 3}
    chances = chances_dict.get(choice, 10)
    print()
    print(f"You have {chances} to guess the correct number.")
    return chances


def game(chances):
    guess = random_number()
    print()
    attempts = 0
    while chances > 0:
        attempts += 1
        user_guess = int(input("Enter your guess: "))
        if user_guess == guess:
            print()
            print(
                f"{GREEN}Congratulations! You guessed the correct number in {attempts} attempts.{RESET}"
            )
            play_again_exit()
        elif user_guess > guess:
            print(f"{YELLOW}Incorrect! The number is less than {user_guess}{RESET}")
        elif user_guess < guess:
            print(f"{YELLOW}Incorrect! The number is greater than {user_guess}{RESET}")
        chances -= 1
    play_again_exit()


def play_again_exit():
    print()
    print("Please select an option")
    print("1. Play Again")
    print("2. Select difficulty level")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        new_guess = random_number()
        game(new_guess)
    elif choice == "2":
        select_difficulty_level()
    elif choice == "3":
        print()
        print(f"{GREEN}Thank you for playing!{RESET}")
        print()
        exit()
    else:
        print(f"{RED}Invalid option. Please try again.{RESET}")
        play_again_exit()


def select_difficulty_level():
    print()
    print("Select a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice: ")
    chances = no_of_chances(choice)
    game(chances)


def random_number():
    return randint(1, 100)


def main():
    print()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    sleep(1)
    select_difficulty_level()


if __name__ == "__main__":
    main()