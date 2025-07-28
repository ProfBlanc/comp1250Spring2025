while True:
    answer = input("Enter a number: ")
    try:
        num = int(answer)
        print(num, "is a valid number")
        break
    except Exception as e:
        print("Sorry but", answer, "is NOT a valid number")
        print("Please try again!")

#print("Thanks, your answer of", num, "has been processed")
