class Calculator:
    def calculate(self, *args):# can accept any number which will not give any error
        # Check if all arguments are integers or floats
        if any(type(arg) not in (int, float) for arg in args):
            raise ValueError("All arguments must be integers or floats.")
        if len(args) == 1:
            return args[0] ** 2
        elif len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] * args[1] * args[2]
        else:
            raise ValueError("Number of arguments must be between 1 and 3.")
calc = Calculator()
try:
    print(calc.calculate(4))          # Output: 16 (square)
    print(calc.calculate(4, 5))       # Output: 9 (sum)
    print(calc.calculate(2, 3, 4))    # Output: 24 (product)
    print(calc.calculate(2, 'a'))     # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")