"""
School Grades Organizer

    Semester
        term: winter, spring, fall
        year
    Grade
        percent
        letter
    Course
        name
        semester
        grade
    School
        school_name
        program_name
        number_of_years
        list of Courses


"""

class Semester:
    def __init__(self, term, year):
        self.term = term
        self.year = year
    def __str__(self):
        return f"{self.term} {self.year} semester"

class Grade:
    def __init__(self, percent):
        self.percent = percent if percent >= 0 and percent <= 100 else 0
        self.letter = self.get_letter()
    def get_letter(self):
        if self.percent >=90 and self.percent <= 100:
            return "A+"
        elif self.percent >= 80:
            return "A"
        elif self.percent >= 70:
            return "B"
        elif self.percent >= 60:
            return "C"
        elif self.percent >= 50:
            return "D"
        else:
            return "F"
    def __str__(self):
        return f"{self.percent}% ({self.letter})"

class Course:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester
        self.grade = None
    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grade = grade

class School:
    def __init__(self, name, program_name, number_of_years):
        self.name = name
        self.program_name = program_name
        self.number_of_years = number_of_years
        self.courses = []
    def add_course(self, course):
        if isinstance(course, Course):
            self.courses.append(course)

    def __str__(self):
        content = ""
        content += f"The school {self.name} has the program {self.program_name}\n"
        content += f"The program {self.program_name} is {self.number_of_years} years\n"
        content += "Here is the list of courses:\n"

        for course in self.courses:
            content += "*" * 20 + "\n"
            content += f"{course.name} is available in {course.semester.term} {course.semester.year}\n"
            content += f"The grade achieved in this course is {course.grade.percent} ({course.grade.letter})\n"
        return content


george_brown_college = School(name="George Brown College",
                              program_name="Computer Systems Technology",
                              number_of_years=3)

semester_two = Semester(term="Spring", year=2025)

python_course = Course(name="Intro to Programming", semester=semester_two)
networking_course = Course(name="Intro to Networking", semester=semester_two)

python_course.add_grade(Grade(90))
networking_course.add_grade(Grade(85))

george_brown_college.add_course(python_course)
george_brown_college.add_course(networking_course)
print(george_brown_college)

