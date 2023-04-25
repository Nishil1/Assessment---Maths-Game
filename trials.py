def num_check(question):
    while True:
        try:
            number = int(input(question))
            return number

        except ValueError:
            print("Please enter a valid integer")
            continue


first_number = num_check("First Number: ")
second_number = num_check("Second Number: ")

print(f"{first_number} + {second_number} = {first_number + second_number}")