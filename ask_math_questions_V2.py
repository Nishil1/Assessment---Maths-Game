# This function is used to obtain how many questions to user wants answer and also validates user guess
def number_checker(question, error, minimum_number=None):
    while True:
        # asks the question
        response = input(question)

        # Checks for emergency exit code
        if response == "xxx":
            return response

        try:
            response = int(response)

            # required_numbers will be none for user guesses and user can guess -tive number so there isn't any
            # restrictions. However, amount of questions has to be > than 0.
            if minimum_number is not None:
                if response >= minimum_number:
                    return response
                else:
                    # if response is not >= minimum_number, gives an error message
                    print(error)
                    continue
            # returns response if minimum is none
            return response
        # if entered value is a float or string/ not an integer, gives an error message
        except ValueError:
            print(error)
