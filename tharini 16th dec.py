#16/12
class System:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def set_password(self):
        if len(self._password) < 8:
            return "Password must contain at least 8 characters"
        elif self._password.isalpha():
            return "Password must contain at least one number"
        elif self._password.isalnum() or ' ' in self._password:
            return "Password must contain at least one symbol"
        else:
            return "Password is valid"

    def check_password(self):
        result = self.set_password()
        if result == "Password is valid":
            print("Password is correct")
        else:
            print(result)

username = input("Enter your username: ")
password = input("Enter your password: ")
s = System(username, password)
s.check_password()
class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Price should be greater than 0")

    def set_stock(self, stock):
        if isinstance(stock, int) and stock > 0:
            self._stock = stock
        else:
            print("Stock must be a positive integer")

    def get_stock(self):
        return self._stock

name = input("Enter the product name: ")
price = int(input("Enter the product price: "))
stock = int(input("Enter the product stock: "))
pt = Product(name, price, stock)
print(f"Stock: {pt.get_stock()}")
class Student:
    def __init__(self, name, age, marks):
        self._name = name
        self._age = age
        self._marks = marks

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_marks(self):
        return self._marks

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if 5 <= age <= 100:
            self._age = age
        else:
            print("Age must be between 5 and 100.")

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Marks must be between 0 and 100.")

    def display_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self._marks = new_marks
        else:
            print("Marks must be between 0 and 100.")

name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
marks = int(input("Enter the student's marks: "))
s = Student(name, age, marks)
print(f"Name: {s.get_name()}")
print(f"Age: {s.get_age()}")
print(f"Marks: {s.get_marks()}")
M_marks = int(input("Enter the new marks to display: "))
s.display_marks(M_marks)
print(f"Display Marks: {s.get_marks()}")
