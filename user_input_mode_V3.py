def choice_checker(question, var_list, error):
    while True:
        # asks question
        var_question = input(question).lower()

        # checks for 2 possible answers
        for items in var_list:
            if var_question == items or var_question == items[0]:
                print("Pass")
                continue

        # if input is invalid
        print(error)


valid_level_list = ["easy", "medium", "hard"]
which_mode = choice_checker("Choose mode: ", valid_level_list, "Please choose easy, medium or hard")