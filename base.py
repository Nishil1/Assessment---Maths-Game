import random
from operator import add, sub, mul



def choice_checker(question, list, error):
    while True:
        response = input(question)
        if response not in list:
            print(error)
        else:
            return response

def num_check(question, error, required_numbers=None):
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



yes_no_list = ["yes", "y", "no", "n"]
show_instructions = choice_checker("Have you played the game before? ", yes_no_list, "Please enter yes/no")

if show_instructions == "no" or show_instructions == "n":
    print("Shows Instructions")

valid_level_list = ["1", "2", "3"]

type_of_level = choice_checker("Choose level: ", valid_level_list,
                               "Please enter a whole integer between 1 and 3")
print(f"You chose level {type_of_level}")

amount_of_questions = num_check("Number of questions: ", "Please enter an integer greater than 0", 1)


amount_of_questions_answered = 0

min_guess = 1
max_guess = 13

level_2_valid_operations = ["+", "-"]
level_3_valid_operations = ["/", "*"]


# Game loop
while amount_of_questions_answered < amount_of_questions:
    # Generate numbers
    first_number, second_number = random.randint(min_guess, max_guess), random.randint(min_guess, max_guess)
    # Checks which level and sets 2nd number limit and randomly chooses operation
    if type_of_level == "1":
        max_guess = 20
        operation = "+"
        answer = add(first_number, second_number)

    elif type_of_level == "2":
        max_guess = 150
        operation = random.choice(level_2_valid_operations)

        # Checks which operation is chosen and gets the answer
        if operation == "+":
            answer = add(first_number, second_number)
        else:
            answer = sub(first_number, second_number)

    elif type_of_level == "3":
        max_guess = 13
        operation = random.choice(level_3_valid_operations)

        # Gets answer for divide/multiply depending on chosen operation
        if operation == "/" and first_number % second_number != 0:
            answer = first_number // second_number

        elif operation == "*":
            answer = first_number * second_number

        else:
            continue
    # Gets user guess
    user_guess = num_check(f"What is {first_number} {operation} {second_number}? ",
                                  "Please enter a whole integer(Can be negative)")
    print()

    # Checks user guess and displays whether right or wrong
    if user_guess == answer:
        print("Your correct!")
    else:
        print("Thats incorrect")
    # Increases number of questions answered
    amount_of_questions_answered += 1
    print()
    # Tells user how many questions are left
    print(f"Questions left: {amount_of_questions - amount_of_questions_answered}")
    print()


