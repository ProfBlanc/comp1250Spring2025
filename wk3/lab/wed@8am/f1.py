
"""

Ask the user for two numbers
Determine if the first number is
divisible by second number and 
vice versa
"""
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

print(f"Is {num1} divisible by {num2} ? {num1 % num2 == 0}")
print(f"Is {num2} divisible by {num1} ? {num2 % num1 == 0}")


