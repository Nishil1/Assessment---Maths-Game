def choice_checker(question, list, error):
    while True:
        response = input(question).lower()
        if response not in list:
            print(error)
        else:
            return response

yes_no_list = ["yes", "y", "no", "n"]
show_instructions = choice_checker("Have you played the game before? ", yes_no_list, "Please enter yes/no")

if show_instructions == "no" or show_instructions == "n":
    print("Shows Instructions")

