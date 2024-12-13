students = [] 
courses = []  
marks = {}  

def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append((student_id, name, dob))

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append((course_id, name))

def input_marks():
    course_id = input("Enter the course ID to input marks: ")
    if not any(course[0] == course_id for course in courses):
        print("Course ID not found!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        student_id, name, _ = student
        mark = float(input(f"Enter marks for {name} (ID: {student_id}): "))
        marks[course_id][student_id] = mark


def list_students():
    print("\nStudents:")
    for student_id, name, dob in students:
        print(f"ID: {student_id}, Name: {name}, DoB: {dob}")

def list_courses():
    print("\nCourses:")
    for course_id, name in courses:
        print(f"ID: {course_id}, Name: {name}")

def show_student_marks():
    course_id = input("Enter the course ID to view marks: ")
    if course_id not in marks:
        print("No marks found for this course!")
        return

    print(f"\nMarks for course: {next(course[1] for course in courses if course[0] == course_id)}")
    for student_id, mark in marks[course_id].items():
        student_name = next(student[1] for student in students if student[0] == student_id)
        print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")

def main():
    while True:
        print("\nMenu:")
        print("1. Input number of students and their information")
        print("2. Input number of courses and their information")
        print("3. Select a course and input marks for students")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a given course")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
