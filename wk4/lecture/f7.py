"""

ask the user for a number
ask the user to find 3 factors of that number

Example: 

Enter a number greater or equal to 16

Enter a factor of 16 (1 or 3 chances)  (fixed loop)
    Tell them whether their answer is correct or incorrect
    store their answers (whether correct or incorrect)
Summarize their answers
"""
print("You will enter a number, then guess 3 factors of that number")
user_number = int(input("Enter an even number greater or equal to 30: "))
if user_number >= 30 and user_number % 2 == 0:
    print("You chose a good number")
else:
    exit(f"Sorry but, {user_number} is invalid")

guesses = list()
correct_guesses = []
for guess in range(3): # ask the user 3 times
    factor_guess = int(input(f"Enter a factor of {user_number}: "))
    if user_number % factor_guess == 0:
        print(factor_guess, "is a factor of", user_number)
        correct_guesses.append(str(factor_guess))  # in case we want to store it as a string
    else:
        print("Sorry, but", factor_guess, "is not a factor of", user_number)
    
    guesses.append(factor_guess)  # stored as int

print("You correctly guesses", len(correct_guesses), "factors of", user_number)
print("All of your guesses are the following", guesses)
