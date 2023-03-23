import random

# Set the range of numbers for the division problem
min_num = 1
max_num = 100

while True:
    # Generate two random numbers within the specified range
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)

    # Ensure that the division problem has a whole number answer
    if num1 % num2 == 0:
        # Generate the division question and prompt the user for an answer
        question = f"What is {num1} ÷ {num2}? "
        user_answer = input(question)

        # Check if the user's answer is correct
        if int(user_answer) == num1 // num2:
            print("Correct!")
        else:
            print("Incorrect. Try again.")
