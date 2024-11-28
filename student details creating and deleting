class Student:
    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
        print(f"Student object created for {self.name}.")

    def display_info(self):
        print("\nStudent Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")

    def __del__(self):
        print(f"Student object for {self.name} is being deleted.")


name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
course = input("Enter student's course: ")
grade = input("Enter student's grade: ")

student = Student(name, age, course, grade)
student.display_info()

del student
