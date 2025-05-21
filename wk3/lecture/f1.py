# 8JAM

grade = int(input("What is your grade percentage? "))
# &&
if grade >= 80 and grade <= 100:
    letter = "A"
    print("Good job")
    print("I love python")
elif grade >= 70:
    letter = "B"
elif grade >= 60:
    letter = "C"
elif grade >=50:
    letter = "D"
else:
    letter = "N/A"

print(f"Your grade of {grade} results in the letter of {letter}")
