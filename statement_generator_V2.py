def statement_generator(statement, decoration, num_sides, num_tb=None):
    if num_tb is None:
        num_tb = len(statement) * len(decoration)

    sides = decoration * num_sides
    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * num_tb

    print(top_bottom)
    print(statement)
    print(top_bottom)
    print()
    return ""



# Welcome statement
statement_generator("Welcome to the legendary maths game", "*", 4)
