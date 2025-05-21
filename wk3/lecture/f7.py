"""
ask the user for 3 integer values all between 10 and 100.
validate the input
"""

user_input = input("Enter three values separated by a space: ")
#50 75 100
if user_input.count(" ") == 2:
    values = user_input.split(" ")
    # print(values[0])
    # print(values[1])
    # print(values[2])
    if values[0].isdigit() and values[1].isdigit() and values[2].isdigit():
        num1 = int(values[0])
        num2 = int(values[1])
        num3 = int(values[2])
        print("Num1 =", num1, "Num2 =", num2, "Num3 =", num3)
        if num1>= 10 and num1 <= 100 and num2 >= 10 and num2 <= 100 and num3 >= 10 and num3 <=100:
            print("Great! You inputted all numerical values within the range of 10 to 100")
        else:
            print("Bad input")
    else:
        print("Sorry but you inputted invalid int values")

else:
    print("Invalid input")
