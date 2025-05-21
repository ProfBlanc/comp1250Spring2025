"""

Ask the user for 2 numbers.
Ask the user for a operations
Calculate the results based on the numbers and operations
E.G.: 
num1? 10
num2? 5
operation (+, -, /, *): *
result = 10 * 5 = 50

"""
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Enter an operator (+, -, *, /)").strip()[0]

result = 0

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
