def user_number_questions(question, error, required_numbers=None):
    while True:
        try:
            response = int(input(question))
            if required_numbers is not None:
                if response >= required_numbers:
                    return response
                else:
                    print(error)
            return response

        except ValueError:
            print(error)

user_number_questions("Guess: ", 'error message')