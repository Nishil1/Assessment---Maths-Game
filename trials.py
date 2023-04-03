# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    # Make string with five chracters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image/text/integer)")
    print()
    print(
        "This program assumes that images are being represents in 24 bit colour (ie: 24 bits per pixel). For text we assume that ascii encoding is being used(8 bits per character.)")
    print()
    print("Complete as many calculations as nessacary, press <enter> at the end of each calculation or any key to quit")
    print()
    return ""


def user_choice():
    valid = True
    while valid:
        response = input("File type (integer / text/ image): ").lower()

        text_ok = ["text", "t", "txt"]
        integer_ok = ["integer", "int", "#", "number"]
        image_ok = ["image", "img", "pix", "picture", "pic"]

        if response in text_ok:
            return "text"
        elif response in integer_ok:
            return "integer"
        elif response in image_ok:
            return "image"
        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for image")
            if want_integer == "":
                return "integer"
            else:
                return "image"
        else:
            print("Please choose a valid file type!")
            print()


def num_check(question, low):
    valid = False
    while not valid:

        error = " please enter an integer that is more than or equal to {}".format(low)

        try:
            # ask user to enter a number

            response = int(input(question))

            # check if the number is more than 0

            if response >= low:
                return response

            # outputs error if the input is invalid

            else:
                print(error)
                print()
        except ValueError:
            print(error)


def text_bits():
    print()

    var_text = input("Enter some text: ")
    var_lenght = len(var_text)
    num_bits = 8 * var_lenght

    print()
    print("\'{}\' has {} characters...".format(var_text, var_lenght))
    print("# of bits is {} * 8...".format(var_lenght))
    print("We need {} of bits to represent {}".format(num_bits, var_text))
    print()

    return ""


def image_bits():
    image_width = num_check("Image Width? ", 1)
    image_height = num_check("Image Height? ", 1)

    num_pixels = image_width * image_height
    num_bits = num_pixels * 24

    print()
    print("# of pixels = {} * {} = {}".format(image_height, image_width, num_pixels))
    print("# of bits = {} * 24 = {}".format(num_pixels, num_bits))


def int_bits():
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_integer)

    num_bits = len(var_binary)

    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""


# Main routine goes here

statement_generator("Bit calculator for integers, text & images", "-")

first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    if data_type == "integer":
        int_bits()
    elif data_type == "image":
        image_bits()
    else:
        text_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()
    if keep_going == "":
        print()

    else:
        print("Thank you for using bit calculator")