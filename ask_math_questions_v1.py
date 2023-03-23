def num_check(question, error, required_numbers=None):
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



user_guess = num_check("What is x + y? ",
                              "Please enter a whole integer(Can be negative)")

print("Pass")