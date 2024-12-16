class User:
    def __init__(self, username):
        self._username = username
        self._password = None

    def set_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in "!@#$%^&*()_+-=[]{};':\",./<>?" for char in password):
            return False
        self._password = password
        return True

    def check_password(self, input_password):
        if self._password is None:
            return False
        return self._password == input_password


username = input("Enter your username: ")
user = User(username)

while True:
    password = input("Enter your password: ")
    if user.set_password(password):
        print("Password set successfully.")
        break  # Exit loop if password is valid
    else:
        print("Invalid password. Please try again.")
password_to_check = input("Enter your password again to check: ")

if user.check_password(password_to_check):
    print("Password check successful.")
else:
    print("Password check failed.")
    
    
    #2
class Product:
    def __init__(self, name, price, stock):
        self._name = name
        if not self.set_price(price):  # Check return value of setter
            raise ValueError("Invalid initial price.")
        if not self.set_stock(stock): # Check return value of setter
            raise ValueError("Invalid initial stock.")

    def set_price(self, price):
        if price <= 0:
            print("Price must be greater than 0.") #Print the error
            return False  # Indicate failure
        self._price = price
        return True  # Indicate success

    def set_stock(self, stock):
        if not isinstance(stock, int) or stock < 0:
            print("Stock must be a non-negative integer.") #Print the error
            return False  # Indicate failure
        self._stock = stock
        return True  # Indicate success

    def get_stock(self):
        return self._stock

    def get_price(self):
        return self._price
    
    def get_name(self):
        return self._name

# Example usage (without try...except):
product = Product("Laptop", 999.99, 10)
print(f"Name: {product.get_name()}")
print(f"Price: {product.get_price()}")
print(f"Stock: {product.get_stock()}")

if not product.set_price(-10):
    print("Price not updated.")

if not product.set_stock(-10):
    print("Stock not updated.")
    
if not product.set_stock(10.5):
    print("Stock not updated.")
    
    #3
class Student:
    def __init__(self):
        self._name = ""
        self._age = 0
        self._marks = 0

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, value):
        self._name = value

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age with validation
    def set_age(self, value):
        if 5 <= value <= 100:
            self._age = value
        else:
            raise ValueError("Age must be between 5 and 100.")

    # Getter for marks
    def get_marks(self):
        return self._marks

    # Setter for marks with validation
    def set_marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100.")

# Example usage
student = Student()
student.set_name("John Doe")
student.set_age(20)
student.set_marks(85)

print(f"Name: {student.get_name()}, Age: {student.get_age()}, Marks: {student.get_marks()}")