import random

def numbers_function():
    print("You selected Numbers...")
    print("Give value 0 for exit...")
    numbers_list = "0123456789"
    max_length = "20"

    print("Please enter the length of password: (max: 20) ")
    pass_length = input()

    if (pass_length == "0"):
        print("Exiting program...")

    def numbers():
        count = 0
        while (count < int(pass_length)):
            random_number = random.randint(0,9)
            print(numbers_list[random_number], end="")
            count = count + 1
        print()

    if pass_length <= max_length:
        numbers()
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
        numbers()