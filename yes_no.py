# Yes/no checker
def yes_no(question):
    while True:

        response = input(question)
        if response == "yes" or response == "y":
            return response
        elif response == "n" or response == "no":
            return response
        else:
            print("Please enter yes/no")

show_instructions = yes_no("Have you played this game before? ")

instructions = "Welcome to the math quiz, you can select levels 1 - 3 in which level 1 where boh numbers are under 20" \
               "addition or subtraction. Level 2 has numbers under 150 and allows addition and subtraction. Level 3 is " \
               "whole number multiplication/division for numbers below 13"
if show_instructions == "no" or show_instructions == "n":
    print(instructions)
