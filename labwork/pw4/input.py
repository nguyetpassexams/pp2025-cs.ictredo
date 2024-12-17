from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def input_students():
    students = []
    for _ in range(int(input("Number of students: "))):
        students.append(Student(input("ID: "), input("Name: "), input("DOB: ")))
    return students

def input_courses():
    courses = []
    for _ in range(int(input("Number of courses: "))):
        courses.append(Course(input("ID: "), input("Name: "), int(input("Credits: "))))
    return courses

def input_marks(students, courses):
    marks = []
    for course in courses:
        print(f"Marks for {course.name}:")
        for student in students:
            marks.append(Mark(student.student_id, course.course_id, float(input(f"{student.name}: "))))
    return marks
