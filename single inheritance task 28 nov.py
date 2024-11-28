#SINGLE INHERITANCE
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
        
class Student(Person):
    def __init__(self,name,student_id):
        super().__init__(name)
        self.student_id=student_id
    def show_stud_id(self):
        print(self.student_id)
student=Student("Tharini",49)
student.show_name()
student.show_stud_id()
