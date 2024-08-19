import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while guess != secret_number:
        try:
            # Prompt the user to enter a guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback based on the guess
            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()