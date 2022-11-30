import random
import uppercase
import lowercase
import number
import symbols
import randoms

print("Welcome to Password Generator")
print(" --- List of available options --- ")

print("Choice 1: Uppercase")
print("Choice 2: Lowercase")
print("Choice 3: Numbers")
print("Choice 4: Symbols")
print("Choice 5: Random")

print("Please select one choice: ")
choice = input()

if (choice == "1"):
	uppercase.uppercase_function()

elif (choice == "2"):
	lowercase.lowercase_function()

elif (choice == "3"):
	number.numbers_function()

elif (choice == "4"):
	symbols.symbols_function()

elif (choice == "5"):
	randoms.randoms_function()

else:
	print("Invalid Choice...")
	print("Ending program...")
