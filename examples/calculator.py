"""
Calculator Example for pyMeow

This example demonstrates basic arithmetic operations and functions.
It shows how pyMeow visualizes mathematical operations and function definitions.

When loaded in pyMeow:
- Each function becomes a pink FunctionBlock with editable name and parameters
- Operations appear as OperationBlocks with dropdown menus for operators
- Return statements become ReturnBlocks showing what value is returned
- The main calculation logic is clearly structured in nested blocks

This example helps learners understand:
- How functions encapsulate reusable code
- How parameters pass data into functions
- How return values send results back
- The flow of mathematical operations
"""

def add(a, b):
    """Add two numbers together."""
    result = a + b
    return result

def subtract(a, b):
    """Subtract b from a."""
    result = a - b
    return result

def multiply(a, b):
    """Multiply two numbers."""
    result = a * b
    return result

def divide(a, b):
    """Divide a by b, with error checking."""
    if b != 0:
        result = a / b
        return result
    else:
        print("Error: Division by zero!")
        return None

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if len(numbers) > 0:
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        return average
    else:
        return 0

# Example usage of the calculator functions
num1 = 10
num2 = 5

# Perform various calculations
sum_result = add(num1, num2)
diff_result = subtract(num1, num2)
product_result = multiply(num1, num2)
quotient_result = divide(num1, num2)

# Print the results
print("Addition:", sum_result)
print("Subtraction:", diff_result)
print("Multiplication:", product_result)
print("Division:", quotient_result)

# Calculate average of multiple numbers
test_numbers = [10, 20, 30, 40, 50]
avg = calculate_average(test_numbers)
print("Average:", avg)