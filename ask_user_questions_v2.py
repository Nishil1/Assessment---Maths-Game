def user_number_questions(question, error, required_numbers=None):
    while True:
        try:
            response = int(input(question))
            if required_numbers is not None:
                if response >= required_numbers:
                    print("Program Continues")
                    return response
                else:
                    print(error)
                    continue
            return response

        except ValueError:
            print(error)

amount_of_questions = user_number_questions("Number of questions: ", "Please enter an integer greater than 0", 1)

