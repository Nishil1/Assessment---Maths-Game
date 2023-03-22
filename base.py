import random
from operator import add, sub, mul



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

range_I = 0
range_II = 0

level_2_valid_operations = ["+", "-"]
level_3_valid_operations = ["/", "*"]

while amount_of_questions_answered < amount_of_questions:
    range_I = 0

    first_number, second_number = random.randint(range_I, range_II), random.randint(range_I, range_II)

    if type_of_level == "1":
        range_II = 20
        operation = "+"
        answer = add(first_number, second_number)

    elif type_of_level == "2":
        range_II = 150
        operation = random.choice(level_2_valid_operations)

        if operation == "+":
            answer = add(first_number, second_number)
        else:
            answer = sub(first_number, second_number)

    elif type_of_level == "3":
        range_II = 13
        operation = random.choice(level_3_valid_operations)

        if operation == "*":
            answer = mul(first_number, second_number)
        else:
            if first_number % second_number == 0:
                answer = first_number // second_number



    guess = user_number_questions(f"What is {first_number} {operation} {second_number}? ",
                                  "Please enter a whole integer(Can be negative)")


    if int(guess) == answer:
        print("Your correct!")
    else:
        print("You lost")

    amount_of_questions_answered += 1


