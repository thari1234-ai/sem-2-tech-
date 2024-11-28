#PARENT CLASS 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print(self.name)
        print(self.salary)
#CHILD CLASS 
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display_department(self):
        print(self.department)
        
manager=Manager("Tharini",10000,"Coding")
manager.display_details()
manager.display_department()

    
        
     
    