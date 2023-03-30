import random


# This function is used for yes/no responses and choice of level responses
def choice_checker(question, var_list, error):
    while True:
        # Takes in the question
        response = input(question).lower()

        # checks if user response is in the given list
        if response not in var_list:
            # if it is not, an error message is printed
            print(error)
        else:
            # if its a valid response, return it
            return response


# This function is used to obtain how many questions to user wants answer and also validates user guess
def user_number_questions(question, error, minimum_number=None):
    while True:
        try:
            # asks the questions
            response = int(input(question))

            # required_numbers will be none for user guesses and user can guess -tive number so there isn't any
            # restrictions. However, amount of questions has to be > than 0.
            if minimum_number is not None:
                if response >= minimum_number:
                    return response
                else:
                    # if response is not >= minimum_number, gives an error message
                    print(error)
                    continue
            # returns response if minimum is none or minimum_number requirement are met
            return response
        # if entered value is a float or string/ not an integer, gives an error message
        except ValueError:
            print(error)


# Meant for aesthetics, this function takes in 2 parameters, the statement and a custom decoration.
# This makes the program look better.
def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    print()
    return ""


# This function is used to convert decimal percentages to a whole number instead of .00
def convert_to_integer(input_number):
    # checks if a float (input_number) is an integer
    if float(input_number).is_integer():
        # in that case return it as a whole number
        return int(input_number)
    else:
        # if the float number is not an integer, return it to 2 decimal places
        return round(input_number, 2)


# Main routine stats here

# Welcome statement
statement_generator("Welcome to the legendary maths game", "*")

# List for yes_no responses
yes_no_list = ["yes", "y", "no", "n"]

# Asks user if they have played the game before
show_instructions = choice_checker("Have you played the game before? ", yes_no_list, "Please enter yes/no")

# Checks if user as not played the game
if show_instructions == "no" or show_instructions == "n":
    # Displays instructions
    print("Shows Instructions")

# List for valid levels that can be chosen by the user
valid_level_list = ["1", "2", "3"]

# Asks the user for a level, uses choice checker function to ensure inputs are valid.
type_of_level = choice_checker("Choose level: ", valid_level_list,
                               "Please enter a whole integer between 1 and 3")
# Displays the level the user chose
print(f"You chose level {type_of_level}")

# Asks the user for the number of questions
amount_of_questions = user_number_questions("Number of questions: ", "Please enter an integer greater than 0", 1)

# Counter for number of questions the user has answered
amount_of_questions_answered = 0

# The minimum number used for all operations aside from division
min_num = 0

# List that contains game history(Correct and Wrong)
game_history = []

# Operation lists for level 2 and 3.
level_2_valid_operations = ["+", "-"]
level_3_valid_operations = ["/", "*"]

# Counter for the number of questions right
questions_right = 0

# Game loop
while amount_of_questions_answered < amount_of_questions:

    # Checks what level the user wants to play, sets the max number and decides the operation
    if type_of_level == "1":
        max_num = 20
        operation = "+"

    elif type_of_level == "2":
        max_num = 150
        operation = random.choice(level_2_valid_operations)

    elif type_of_level == "3":

        # decides max number for level 3
        max_num = 13
        operation = random.choice(level_3_valid_operations)
        # used to fix warning that max_num could be undefined
    else:
        max_num = ""
        operation = ""

    # Generates two random numbers using min_num and max_num for operations.
    first_number, second_number = random.randint(min_num, max_num), random.randint(min_num, max_num)

    # Gets the answer depending on the operation, uses eval to evaluate the answer.
    if operation == "*":
        answer = eval("first_number * second_number")
    elif operation == "/" and first_number % second_number == 0:
        # Sets the minimum number to 0 to avoid ZeroDivisionError
        min_num = 1
        answer = eval("first_number // second_number")
    elif operation == "-":
        answer = eval("first_number - second_number")
    elif operation == "+":
        answer = eval("first_number + second_number")
        # To avoid warning of answer may be undefined
    else:
        continue

    # Gets the user_guess and uses user_number_questions to validate the user input
    user_guess = user_number_questions(f"What is {first_number} {operation} {second_number}? ",
                                       "Please enter a whole integer(Can be negative)")
    print()

    # Checks if user is correct
    if user_guess == answer:
        # Displays a correct message telling the user that their guess is correct
        print("Your correct!")
        # Increases questions_right by 1
        questions_right += 1
        # Adds feedback(To be displayed at end of game)
        feedback = f"Question {amount_of_questions_answered + 1}: Correct!"

    # if user is wrong
    else:
        # Alerts the user that their guess is incorrect
        print("That's incorrect")
        # Adds feedback(To be displayed at end of game)
        feedback = f"Question {amount_of_questions_answered + 1}: " \
                   f"Wrong. {first_number} {operation} {second_number} is not {user_guess}, it is {answer}"

    # Appends feedback to the game_history list which will be displayed after the game finishes
    game_history.append(feedback)
    # Increases the amount of questions answered by 1
    amount_of_questions_answered += 1
    print()

    # Checks if the number of questions left is > than or equal to 1, which in that case display # of questions left.
    # If not, then continue
    if amount_of_questions - amount_of_questions_answered >= 1:
        print(f"Questions left: {amount_of_questions - amount_of_questions_answered}")
    print()

# Title for game history using statement_generator function to make code look visually appealing
statement_generator("Game history", "-")

# DDisplays game history using a for loop
for item in game_history:
    print(item)

print()

# Calculates the percentage the user got right
percentage_right = questions_right / amount_of_questions * 100

# Displays game summary title using statement_generator function to make code look visually appealing
statement_generator("Game Summary", "*")

# Displays percentage of right and wrong, calculates percentage wrong by taking away percentage right by 100
print(f"You got {convert_to_integer(percentage_right)}% right and "
      f"{convert_to_integer(100 - percentage_right)}% wrong.")

print()

# Thanks the user for playing using a quit statement instead of print statement as it displays the text in red which I
# liked
print("Thanks for playing")