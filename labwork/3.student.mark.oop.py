import math
import numpy as np
import curses

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []  
        self.gpa = 0.0

    
    def input_marks(self, stdscr):
        stdscr.clear()
        stdscr.addstr(f"Enter marks for {self.name}\n")
        num_subjects = int(self.get_input(stdscr, "Number of subjects: "))

        for i in range(num_subjects):
            mark = float(self.get_input(stdscr, f"Enter score for subject {i + 1}: "))
            rounded_mark = math.floor(mark * 10) / 10.0 

            credit = float(self.get_input(stdscr, f"Enter credit for subject {i + 1}: "))
            self.scores.append((rounded_mark, credit))

        self.calculate_gpa()
        stdscr.addstr("\nMarks and credits added successfully!\n")
        stdscr.getch()

    def get_input(self, stdscr, prompt):
        stdscr.addstr(prompt)
        stdscr.refresh()
        curses.echo()
        user_input = stdscr.getstr().decode("utf-8")
        curses.noecho()
        return user_input

    def calculate_gpa(self):
        if not self.scores:
            self.gpa = 0.0
            return

        marks = np.array([score[0] for score in self.scores])  
        credits = np.array([score[1] for score in self.scores])  

        weighted_sum = np.sum(marks * credits)  
        total_credits = np.sum(credits)
        self.gpa = weighted_sum / total_credits if total_credits > 0 else 0.0

    def list_marks(self, stdscr):
        stdscr.addstr(f"\nStudent: {self.name}\n")
        for i, (mark, credit) in enumerate(self.scores):
            stdscr.addstr(f"Subject {i + 1} -> Score: {mark}, Credit: {credit}\n")
        stdscr.addstr(f"Average GPA: {self.gpa:.2f}\n")

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(Student(name))

    def sort_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)

    def input_all_students(self, stdscr):
        for student in self.students:
            student.input_marks(stdscr)

    def display_all(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Student List Sorted by GPA:\n")
        self.sort_by_gpa()  # Sort students by GPA
        for student in self.students:
            student.list_marks(stdscr)
        stdscr.addstr("\nPress any key to continue...")
        stdscr.getch()

def main(stdscr):
    curses.curs_set(0)  
    stdscr.clear()

    classroom = Classroom()

    stdscr.addstr("Welcome to Student Marks Management System\n")
    stdscr.addstr("Enter number of students: ")
    curses.echo()
    num_students = int(stdscr.getstr().decode("utf-8"))
    curses.noecho()

    for i in range(num_students):
        stdscr.addstr(f"Enter name for student {i + 1}: ")
        name = stdscr.getstr().decode("utf-8")
        classroom.add_student(name)

    classroom.input_all_students(stdscr)
    classroom.display_all(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
