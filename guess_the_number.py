import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    print("Welcome to Guess the Number Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
           
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue  # Do not count this attempt

            attempts += 1  # Count the attempt only after valid input

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                return  # Exit the function if guessed correctly

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            # Don't count this attempt

    # Only show this message if the user did not guess correctly
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
