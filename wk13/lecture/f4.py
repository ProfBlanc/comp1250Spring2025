answer = input("Enter a whole number greater than 10: ")

try:
    num = int(answer)  # good, but would accept ANY number
    if num <= 10:
        raise ValueError("Invalid number. Number isn't greater than 10")
    print("Thank you. Your number of", num, "is valid")
except Exception as e:
    print("Sorry but", answer, "is an invalid answer")
    print(e)
