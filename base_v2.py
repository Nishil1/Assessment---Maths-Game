import random



def choice_checker(question, list, error):
    while True:
        response = input(question)
        if response not in list:
            print(error)
        else:
            return response


def user_number_questions(question, error, required_numbers=None):
    while True:
        try:
            response = int(input(question))
            if required_numbers is not None:
                if response >= required_numbers:
                    return response
                else:
                    print(error)
                    continue
            return response

        except ValueError:
            print(error)


def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    print()
    return ""


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

min_num = 0
max_num = 20

game_history = []

level_2_valid_operations = ["+", "-"]
level_3_valid_operations = ["/", "*"]

while amount_of_questions_answered < amount_of_questions:

    first_number, second_number = random.randint(min_num, max_num), random.randint(min_num, max_num)

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

    if operation == "*":
        answer = eval("Fir")
    elif operation == "/" and first_number % second_number == 0:
        min_num = 1
        answer = first_number // second_number
    elif operation == "-":
        answer = sub(first_number, second_number)
    elif operation == "+":
        answer = add(first_number, second_number)
    else:
        continue

    guess = user_number_questions(f"What is {first_number} {operation} {second_number}? ",
                                  "Please enter a whole integer(Can be negative)")
    print()

    if guess == answer:
        print("Your correct!")
        feedback = f"Question {amount_of_questions_answered + 1}: Correct!"
    else:
        print("Thats incorrect")
        feedback = f"Question {amount_of_questions_answered + 1}: " \
                   f"Wrong. {first_number} {operation} {second_number} is not {guess}. It is {answer}"

    game_history.append(feedback)
    amount_of_questions_answered += 1
    print()

    if amount_of_questions - amount_of_questions_answered >= 1:
        print(f"Questions left: {amount_of_questions - amount_of_questions_answered}")
    print()

statement_generator("Game history", "-")

for item in game_history:
    print(item)
