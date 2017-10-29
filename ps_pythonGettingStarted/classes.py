
# CREATE STUDENTS in db

students = []

class Student:
    def __init__(self, name, student_id=332):  # initialiization
        student = {"name": name, "student_id": student_id}
        students.append(student)

mark = Student("Mark")

print(students)

