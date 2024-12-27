#parameterized constructor
class student:
    def __init__ (self,name,dept="ai"):
        self.name=name
        self.dept=dept
    def display(self):#
        print(self.name)
        print(self.dept)
    def __del__(self):#destructor method
        print("obj destroyed")
stu=student("haha")
stu.display()
del stu

