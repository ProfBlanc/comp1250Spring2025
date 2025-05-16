
# ask the user for three grades.
# repeat the code 
# output the min grade, max grade and average grade

print("Welcome to our app. I will ask you for 3 grades and will output", end=' ')
print("the min grade, max grade and average grade")

grade1 = int(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = input("Enter the third grade: ")
grade3 = float(grade3)

print(f"The lowest grade is {min(grade1, grade2, grade3)}")
print("The higest grade is", max(grade1, grade2, grade3))
print(f"The average grade of {grade1}, {grade2} & {grade3} is", 
(grade1 + grade2 + grade3) / 3)
