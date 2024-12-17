from input import input_students, input_courses, input_marks
from output import display_students, display_courses, display_marks

def main():
    students = input_students()
    courses = input_courses()
    marks = input_marks(students, courses)
    display_students(students)
    display_courses(courses)
    display_marks(marks)

if __name__ == "__main__":
    main()
