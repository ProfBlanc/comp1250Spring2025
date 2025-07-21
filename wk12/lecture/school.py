class Grade:
    # letter
    # percent
    def __init__(self, percent):
        self.percent = percent if percent >= 0 and percent <= 100 else 0
        self.letter = self.get_grade_letter()

    def get_grade_letter(self):
        if self.percent >=90 and self.percent <= 100:
            return "A"
        elif self.percent == 0:
            return "???"
        else:
            return "Some letter between B and F"
class Student:
    def __init__(self, name: str, grade: Grade = None):
        self.name = name
        self.grade = grade if grade is not None else Grade(0)
        # if grade is None:
        #     self.grade = Grade(0)
        # else:
        #     self.grade = grade
    def __str__(self):
        return "Student's name is " + self.name

class Course:
    def __init__(self, name: str, students: list[Student]):
        self.name = name
        self.students = students

    def __str__(self):
        return f"The course {self.name} has " \
               f"{len(self.students)} students"


s1 = Student("John", Grade(99))
s2 = Student("Mary", Grade(98))
s3 = Student("Peter")
s4 = Student("Jill")

students = list()
students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)

comp1250 = Course("Intro to Programming", students)
print(comp1250)
#print out the name of the second student
print(comp1250.students[1].name)
print(comp1250.students[1].grade.letter)
print(comp1250.students[1].grade.percent)

my_grade = Grade(110)
print(my_grade.letter)