class Calculator:
    def calculate(self, a, b=0, c=0):
        for i in (a, b, c):
            if type(i) not in (int, float):
                raise ValueError("All inputs must be integers or floats")
        
        if a != 0 and b != 0 and c != 0:
            return a * b * c
        elif a != 0 and b != 0 and c == 0:
            return a + b
        elif a != 0 and b == 0 and c == 0:
            return a ** 2
        else:
            return "Invalid input"

# Testing the Calculator class
c = Calculator()
try:
    print(c.calculate(2))          # Expected output: 4 (2^2)
    print(c.calculate(2, 3))       # Expected output: 5 (2 + 3)
    print(c.calculate(2, 3, 4))    # Expected output: 24 (2 * 3 * 4)
    print(c.calculate(2, 3, "4"))  # Should raise ValueError
except ValueError as e:
    print(e)
