
# CREATE STUDENTS in db

students = []

class Student:
    def __init__(self, name, student_id=332):  # initialiization
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

mark = Student("Mark")
print(mark)

#print(students)