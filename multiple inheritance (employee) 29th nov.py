#multiple inheritance->many parent class one child class 
class Employee:
    def __init__(self,name,Id,position):
        self.name=name
        self.Id=Id
        self.position=position
    def display_employeeinfo (self):
        print(self.name)
        print(self.Id)
        print(self.position)
        
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def display_address(self):
        print(self.street)
        print(self.state)
        print(self.country)
        
class Employeedetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):
        super().__init__(name,Id,position)
        Address.__init__(self,street,state,country)
    def display_employee(self):
        self.display_employeeinfo()
        self.display_address()
        
e=Employeedetails("Thari",49,"manager","lenin nagar","tn","india")
e.display_employee() 
        
        