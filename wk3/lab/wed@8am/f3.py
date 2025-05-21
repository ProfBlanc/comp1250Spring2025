"""
# Task 1
user_input = input("Enter a number: ")
print(user_input.isnumeric())

Ask the user for 2 numbers.
Ask the user for a operations
Calculate the results based on the numbers and operations
E.G.: 
num1? 10
num2? 5
operation (+, -, /, *): *
result = 10 * 5 = 50
# Task 2
user_input = input("Enter a string: ")
print(user_input.istitle())
print(user_input.upper())

"""
# Task 3
text_input = input("Enter some text: ")
char_input = input("Enter a character to find: ")

found = char_input in text_input
print(found)

if found:
    print("First position:", text_input.find(char_input))

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Enter an operator (+, -, *, /)").strip()[0]

result = 0

# Task 4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 ** num2
print(f"{num1} raised to the power of {num2} is {result}")


if operator in '+-/*':
    if operator == "+":
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/" and not num2 == 0:
        result = num1 / num2
    
    #print(f"{num1} {operator} {num2} = {result}")
    print(num1, operator, num2, "=", result)
else:
    print("Invalid operator chosen")

# Task 5
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Yes, {year} is a leap year")
        else:
            print(f"No, {year} is not a leap year")
    else:
        print(f"Yes, {year} is a leap year")
else:
    print(f"No, {year} is not a leap year")

# Task 6
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is neutral (zero).")

# Task 7
letter = input("Enter a letter: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u']

if letter in vowels:
    print(f"Yes, '{letter}' is a vowel.")
else:
    print(f"No, '{letter}' is not a vowel.")



