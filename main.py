from random import randint
from time import sleep


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
                f"Congratulations! You guessed the correct number in {attempts} attempts."
            )
            play_again_exit()
        elif user_guess > guess:
            print(f"Incorrect! The number is less than {user_guess}")
        elif user_guess < guess:
            print(f"Incorrect! The number is greater than {user_guess}")
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
        print("Thank you for playing!")
        print()
        exit()
    else:
        print("Invalid option. Please try again.")
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