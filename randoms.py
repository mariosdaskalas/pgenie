import random

def randoms_function():

    print("You selected Random...")
    print("Give value 0 for exit...")

    all = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
    max_length = "20"

    print("Please enter the length of password: (max: 20) ")
    pass_length = input()

    if (pass_length == "0"):
        print("Exiting program...")

    def alls():
        count = 0
        while (count < int(pass_length)):
            random_all = random.randint(0,92)
            print(all[random_all], end="")
            count = count + 1
        print()

    if pass_length <= max_length:
        alls()
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
        alls()