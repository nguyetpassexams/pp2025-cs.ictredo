class Student:
    def __init__(self, name, marks=None):
        self.name = name
        self._marks = marks if marks else []  
        
    def _set_marks(self, marks):
        self._marks = marks

    def input(self):
        number_of_subjects = int(input(f"How many subjects does {self.name} have? "))
        for i in range(number_of_subjects):
            mark = float(input(f"Enter mark for subject {i + 1}: "))
            self._marks.append(mark)

    def calculate_average(self):
        if len(self._marks) == 0:
            return 0
        return sum(self._marks) / len(self._marks)

    def list(self):
        print(f"Marks for {self.name}: {self._marks}")
        print(f"Average: {self.calculate_average():.2f}")

    def update_marks(self, marks):
        self._set_marks(marks)

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all(self):
        for student in self.students:
            student.list()
            
if __name__ == "__main__":
   
    student1 = Student("Alice")
    student2 = Student("Bob")
    
    student1.input()
    student2.input()

    classroom = Classroom()

    classroom.add_student(student1)
    classroom.add_student(student2)

    classroom.display_all()
