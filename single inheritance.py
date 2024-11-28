#single inheritance 
# Parent class
class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(f"Name: {self.name}")
# Child class inheriting from Person
class Student(Person):
    def __init__(self, name, student_id):
        # Call the constructor of the parent class
        super().__init__(name)
        self.student_id = student_id 
    def show_student_id(self):
        print(f"Student ID: {self.student_id}")
student = Student("Alice", "S12345")
student.show_name()  # Call the method from the parent class
student.show_student_id()  # Call the method from the child class
