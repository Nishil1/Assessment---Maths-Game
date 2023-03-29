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
def user_number_questions(question, error, minumum_number=None):
    while True:
        try:
            # asks the questions
            response = int(input(question))

            # required_numbers will be none for user guesses and user can guess -tive number so there isnt any
            # restrictions. However, amount of questions has to be > than 0.
            if minumum_number is not None:
                if response >= minumum_number:
                    return response
                else:
                    # if response is not >= minimum_number, gives an error message
                    print(error)
                    continue
            # returns response if minumum_number is none or minimum_number requirement are met
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
        # if the float number is not a integer
        return input_number


# Main routine stats here

statement_generator("Welcome to the legendary maths game", "*")

yes_no_list = ["yes", "y", "no", "n"]
show_instructions = choice_checker("Have you played the game before? ", yes_no_list, "Please enter yes/no")

if show_instructions == "no" or show_instructions == "n":
    print("Shows Instructions")

valid_level_list = ["1", "2", "3"]

type_of_level = choice_checker("Choose level: ", valid_level_list,
                               "Please enter a whole integer between 1 and 3")
print(f"You chose level {type_of_level}")

amount_of_questions = user_number_questions("Number of questions: ", "Please enter an integer greater than 0", 1)

amount_of_questions_answered = 0

min_num = 1


game_history = []

level_2_valid_operations = ["+", "-"]
level_3_valid_operations = ["/", "*"]

questions_right = 0

while amount_of_questions_answered < amount_of_questions:



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

    first_number, second_number = random.randint(min_num, max_num), random.randint(min_num, max_num)

    if operation == "*":
        answer = eval("first_number * second_number")
    elif operation == "/" and first_number % second_number == 0:
        min_num = 1
        answer = eval("first_number // second_number")
    elif operation == "-":
        answer = eval("first_number - second_number")
    elif operation == "+":
        answer = eval("first_number + second_number")
    else:
        continue

    guess = user_number_questions(f"What is {first_number} {operation} {second_number}? ",
                                  "Please enter a whole integer(Can be negative)")
    print()

    if guess == answer:
        print("Your correct!")
        questions_right += 1
        feedback = f"Question {amount_of_questions_answered + 1}: Correct!"

    else:
        print("Thats incorrect")
        feedback = f"Question {amount_of_questions_answered + 1}: " \
                   f"Wrong. {first_number} {operation} {second_number} is not {guess}, it is {answer}"

    game_history.append(feedback)
    amount_of_questions_answered += 1
    print()

    if amount_of_questions - amount_of_questions_answered >= 1:
        print(f"Questions left: {amount_of_questions - amount_of_questions_answered}")
    print()

statement_generator("Game history", "-")

for item in game_history:
    print(item)

print()

percentage_right = questions_right / amount_of_questions * 100

statement_generator("Game Summary", "*")

print(f"You got {convert_to_integer(percentage_right):.2f}% right and "
      f"{convert_to_integer(100 - percentage_right):.2f}% wrong.")
