# Yes/no checker
def yes_no(question):
    while True:

        response = input(question).lower()
        if response == "yes" or response == "y":
            print("Program Continues")
        elif response == "n" or response == "no":
            print("Shows Instructions")
        else:
            print("Please enter yes/no")

# Asks question to user
show_instructions = yes_no("Have you played this game before? ")

# Instructions information
instructions = "Welcome to the math quiz, you can select levels 1 - 3 " \
               "in which level 1 where boh numbers are under 20"
instructions_I = "addition or subtraction. Level 2 has numbers under " \
                 "150 and allows addition and subtraction. Level 3 is "
instructions_II = "whole number multiplication/division for numbers below 13"

# if user hasnt played game before, show instructions
if show_instructions == "no":
    print(instructions)
    print(instructions_I)
    print(instructions_II)
