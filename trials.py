import random
import math


# checks for valid numbers for lower, higher and user guess
def num_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"

    while True:
        try:
            var_response = int(input(question))
            if situation == "both":
                # check if user input is valid
                if var_response < low or var_response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue
                    # checks whether the high number is greater than low number
            elif situation == "low only":
                if var_response < low:
                    print(f"Please enter a number that is more than or equal to {low}")
                    continue
                    # returns response if all above conditions are met
            return var_response
        # checks for Value error
        except ValueError:
            print("Please enter an integer")
            continue


# Instructions function
def yes_no(question):
    while True:
        # asks question
        var_question = input(question).lower()

        # checks for 2 possible answers
        if var_question == "yes" or var_question == "y":
            return
        elif var_question == "no" or var_question == "n":
            return "no"
        # if input is invalid
        else:
            print("Please enter yes/no")


# Main routine starts here
print("***************************************")
print("**** Welcome to Higher, lower game ****")
print("***************************************")
print()
print()

# Instructions information/message
instructions = "Enter a higher and a lower number, " \
               "a secret number will be randomly generated with limited amount of guesses. " \
               "Can you win the game?"

# shows instructions
response = yes_no("Have you played the game before? ")

# checks whether to show instructions
if response == "no":
    print(instructions)

# Game history list
game_history = []

# ask use for number of rounds
decided_number_of_rounds = num_check("How many rounds: ", low=1)

# Variables counting rounds played & number of guesses done
number_of_rounds_played = 1
number_of_guesses_done = 0

# Gets the higher & lower numbers
lower_number = num_check("Lower number: ")
higher_number = num_check("Higher number: ", lower_number + 1)


# Calculate number of guesses allowed
ranges = higher_number - lower_number + 1
max_raw = math.log2(ranges)
max_upped = math.ceil(max_raw)
maximum_guesses = max_upped + 1

game_stats_numbers = []

# Game loop
while number_of_rounds_played <= decided_number_of_rounds:
    # Displays rounds number & number of guesses available to the user
    print(f"--------------- Round: {number_of_rounds_played} ---------------")
    print(f"Number of guesses: {maximum_guesses}")
    number_of_guesses_done = 0
    user_guessed_number = 0

    # already guessed list, makes sure no duplicates are entered
    already_guessed = []

    # Generates secret number f or user to guess
    secret_number = random.randint(lower_number, higher_number)


    while number_of_guesses_done < maximum_guesses and user_guessed_number != secret_number:

        feedback = ""

        # Takes user guess
        user_guessed_number = num_check("Guess: ", lower_number, higher_number)

        # Checks for duplicates & outputs error if found
        if user_guessed_number in already_guessed:
            print("Oops you already guessed that, try another!")
            continue
        # Adds user guesses to already_guessed list to avoid duplicates
        already_guessed.append(user_guessed_number)
        number_of_guesses_done += 1

        # Checks for possible outcomes, low, high & wins
        if user_guessed_number < secret_number:
            print("***** Too low *****")
            print()
        elif user_guessed_number > secret_number:
            print("***** Too high *****")
            print()
        elif user_guessed_number == secret_number:
            print("!!!!! You got it !!!!!")
            print()
            # Adds user won to game history
            feedback = f"Round {number_of_rounds_played}: Won ({len(already_guessed)} guesses)"
            feedback_I = len(already_guessed)
            break

        # Tells user updated number of guesses left
        print(f"Guesses left: {maximum_guesses - number_of_guesses_done}")

    # If user runs out of guesses
    if number_of_guesses_done == maximum_guesses and user_guessed_number != secret_number:
        print("Sorry you have run out of guesses!")
        print(f"The Secret Number was {secret_number}!!")
        # Adds user lost to game history
        feedback = f"Round {number_of_rounds_played}: Lost (ran out of guesses)"
        feedback_I = maximum_guesses

    game_history.append(feedback)
    game_stats_numbers.append(feedback_I)
    number_of_rounds_played += 1

# End of game(Thanks user & Game History)
print()
print()
print("**** Game History ****")
print()
for item in game_history:
    print(item)
print()

# Game statistics
game_stats_numbers.sort()
best = game_stats_numbers[0]

# Display Game Statistics
print(f"Best: {best}")
print(f"Worst: {game_stats_numbers[-1]}")
average = sum(game_stats_numbers) / len(game_stats_numbers)
print(f"Average: {average}")

quit("Thanks for playing")
