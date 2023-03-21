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

def random_numbers(range_1, range_2, first_number, second_number):
    first_number = random.randint(range_1,range_2)
    second_number = random.randint(range_1, range_2)

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

while amount_of_questions_answered <= amount_of_questions:
    first_number = random.randint()

    if type_of_level == "1":


    elif type_of_level == "2":







