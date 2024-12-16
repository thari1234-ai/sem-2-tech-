class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
        
name=input()
age=int(input())
s=Student(name,age)

print(s.get_name())
print(s.get_age())