
# CREATE STUDENTS in db

students = []

class Student:

    # adding static variable (class attribute) ~ as opposed to instance attributes
    school_name = "Central Elementary"

# function adds self [instance attribute] value to "students"
    def __init__(self, name, student_id=332):  # initialiization
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    # create a function that returns school name
    def get_school_name(self):
        return self.school_name

class HighSchoolStudent(Student): # "Student" is the parent class

    school_name = "Hampton High School"

    def get_school_name(self):
        return "This is a High School Student"

james = HighSchoolStudent("james") # calling (methond/class) HighSchoolStudent
print(james.get_school_name())  # return results via get_school_name function

#mark = Student("Mark")
#print(mark)

#print(students)