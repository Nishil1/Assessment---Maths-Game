import random


# This function is used for yes/no responses and choice of level responses
def choice_checker(question, var_list, error):
    while True:
        # asks question
        var_question = input(question).lower()

        # checks for 2 possible answers
        for items in var_list:
            if var_question == items or var_question == items[0]:
                return items
        # if input is invalid
        print(error)


# This function is used to obtain how many questions to user wants answer and also validates user guess
def number_checker(question, valid_xxx_usage, error, minimum_number=None):
    while True:
        # asks the question
        response = input(question).lower()

        # Checks for emergency exit code
        if response == "xxx" and response == valid_xxx_usage:
            return response

        try:
            response = int(response)

            # required_numbers will be none for user guesses and user can guess -tive number so there isn't a
            # restrictions. However, amount of questions has to be > than 0.
            if minimum_number is not None:
                if response >= minimum_number:
                    return response
                else:
                    # if response is not >= minimum_number, gives an error message
                    print(error)
                    continue
            # returns response if minimum is none
            return response
        # if entered value is a float or string/ not an integer, gives an error message
        except ValueError:
            print(error)


# Meant for aesthetics, this function takes in 4 parameters which I can control what decoration and how much for
# messages I need. Makes things look better.
def statement_generator(statement, decoration, num_sides, num_tb=None):
    if num_tb is None:
        num_tb = len(statement) * len(decoration)

    sides = decoration * num_sides
    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * num_tb

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


# This function is used to convert decimal percentages to a whole number instead of .00
def convert_to_integer(input_number):
    # checks if the decimal number is an integer
    if float(input_number).is_integer():
        # in that case return it as a whole number
        return int(input_number)

    else:
        # if the float number is not an integer, return it to 2 decimal places
        return round(input_number, 2)


# Main routine stats here

# Welcome statement
statement_generator("Welcome to the legendary maths game", "*", 0)

# List for yes_no responses
yes_no_list = ["yes", "no"]

# Asks user if they have played the game before
show_instructions = choice_checker("Have you played the game before? ", yes_no_list, "Please enter yes/no")

# Checks if user as not played the game
if show_instructions == "no":
    # Displays instructions
    print()
    print("Welcome to the game, you can choose what level you want to play(Easy, medium and hard)")
    print("Easy: Addition sums up to 20")
    print("Medium: Addition and subtraction up to 150(can include negative answers)")
    print("Hard: Multiplication and division up to 13 times table")
    print()

# List for valid levels that can be chosen by the user
valid_level_list = ["easy", "medium", "hard"]

# List that contains game history(Correct and Wrong)
game_history = []

# Operation lists for level 2 and 3.
level_2_valid_operations = ["+", "-"]
level_3_valid_operations = ["÷", "x"]

# Asks the user for a level, uses choice checker function to ensure inputs are valid.
which_mode = choice_checker("Choose Mode(Easy, Medium and Hard): ", valid_level_list,
                            "Please choose easy, medium or hard")

# Displays the level the user chose
statement_generator(f"You chose {which_mode} mode", "#", 4, 0)

# Asks the user for the number of questions
amount_of_questions = number_checker("Number of questions: ", "", "Please enter an integer greater than 0", 1)

# Counter for number of questions the user has answered
amount_of_questions_answered = 0

# The minimum number used for all operations
min_num = 1

# Counter for the number of questions right
questions_right = 0

# Game loop
while amount_of_questions_answered < amount_of_questions:

    # Checks what level the user wants to play, sets the max number and decides the operation
    if which_mode == "easy":
        max_num = 20
        operation = "+"

    elif which_mode == "medium":
        max_num = 150
        operation = random.choice(level_2_valid_operations)

    elif which_mode == "hard":
        max_num = 13
        operation = random.choice(level_3_valid_operations)
        # used to fix warning that max_num could be undefined
    else:
        max_num = ""
        operation = ""

    # Generates two random numbers using min_num and max_num for operations.
    first_number, second_number = random.randint(min_num, max_num), random.randint(min_num, max_num)

    # Gets the answer depending on the operation
    if operation == "x":
        answer = first_number * second_number

    elif operation == "÷":
        # uses multiplication to get division questions up to 13, question will be result divided by second number
        # which also means the first number will be the answer
        result = first_number * second_number
        answer = first_number
        first_number = result

    elif operation == "-":
        answer = first_number - second_number
    elif operation == "+":
        answer = first_number + second_number
        # if division generated is not a whole number result, regenerate the numbers
    else:
        continue

    # Displays what question the user is on
    print(statement_generator(f"Question {amount_of_questions_answered + 1}", "#", 4, 0))

    # Gets the user_guess and uses user_number_questions to validate the user input
    user_guess = number_checker(f"What is {first_number} {operation} {second_number}?(Enter 'xxx' to quit') ", "xxx",
                                "Please enter a whole integer(Can be negative)")

    # Check for xxx user exit code
    if user_guess == "xxx":
        break

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

# Makes sure user has answered at least 1 question
if amount_of_questions_answered > 0:

    # Title for game history using statement_generator function to make code look visually appealing
    statement_generator("Game History", "-", 4, 0)

    # Displays game history using a for loop
    for item in game_history:
        print(item)

    print()

    # Calculates the percentage the user got right
    percentage_right = questions_right / amount_of_questions_answered * 100

    # Displays game summary title using statement_generator function to make code look visually appealing
    statement_generator("Game Summary", "*", 4, 0)

    # Displays percentage of right and wrong, calculates percentage wrong by taking away percentage right by 100
    print(f"You got {convert_to_integer(percentage_right)}% right and "
          f"{convert_to_integer(100 - percentage_right)}% wrong.")

    # if user has not answered least 1 question
else:
    print()
    print("There is no history")
print()

# Thanks the user for playing the game
print("Thanks for playing")
