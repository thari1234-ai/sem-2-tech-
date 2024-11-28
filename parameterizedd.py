#parameterized constructor
class student:
    def __init__ (self,name,dept):
        self.name=name
        self.dept=dept
    def display(self):
        print(self.name)
        print(self.dept)
stu=student("haha","AI")
stu.display()