def user_number_questions(question):
    while True:
        try:
            response = int(input(question))

            if response >= 1:
                return response
            else:
                print("Please enter a valid whole number")
        except ValueError:
            print("Please enter a valid whole number")



number_of_questions = user_number_questions("Number of questions: ")
