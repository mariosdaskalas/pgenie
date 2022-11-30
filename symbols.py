import random

def symbols_function():

    print("You selected Symbols...")
    print("Give value 0 for exit...")
    symbols = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
    max_length = "20"

    print("Please enter the length of password: (max: 20) ")
    pass_length = input()

    if (pass_length == "0"):
        print("Exiting program...")

    def symbol():
        count = 0
        while (count < int(pass_length)):
            random_symbol = random.randint(0,30)
            print(symbols[random_symbol], end="")
            count = count + 1
        print()

    if pass_length <= max_length:
        symbol()
    elif (pass_length == "0"):
        print("Exiting program...")
    else:
        print("Please enter a number less or equal to 20.")
        pass_length = input()
        if (pass_length == "0"):
            print("Exiting program...")
        while (pass_length > max_length):
            print("Please enter a number less or equal to 20.")
            pass_length = input()
            if (pass_length == "0"):
                print("Exiting program...")
        symbol()