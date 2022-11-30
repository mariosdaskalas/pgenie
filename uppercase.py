import random

def uppercase_function():
    print("You selected Uppercase.")
    print("Give value 0 for exit...")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    max_length = "20"

    print("Please enter the length of password: (max: 20) ")
    pass_length = input()

    if (pass_length == "0"):
        print("Exiting program...")

    def uppercase():
        count = 0
        while (count < int(pass_length)):
            random_letter = random.randint(0,25)
            print(letters[random_letter], end="")
            count = count + 1
        print()
        
    if pass_length <= max_length:
        uppercase()
    elif (pass_length == "0"):
        print("Exiting program..")
    else:
        print("Please enter a number less or equal to 20.")
        pass_length = input()
        if (pass_length == "0"):
            print("Exiting program..")
        while (pass_length > max_length):
            print("Please enter a number less or equal to 20.")
            pass_length = input()
            if (pass_length == "0"):
                print("Exiting program..")
        uppercase()