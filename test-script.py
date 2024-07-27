# Sample Python code for testing

def add(a, b):
    """Add two numbers."""
    return a + b

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def multiply(self, a, b):
        return a * b

def print_result(value):
    """Print the result."""
    print(f"Result: {value}")

x = 5
y = 10
calc = Calculator()
sum_result = calc.add(x, y)
product_result = calc.multiply(x, y)
print_result(sum_result)
print_result(product_result)
