import random
def num_check(question):
    while True:
        try:
            response = input(question)
            if 3 >= response >= 1:
                return response
            else:
                print("Please enter a whole integer between 1 and 3")
        except ValueError:
            print("Please enter a whole integer between 1 and 3")


level = num_check("Choose level: ")

