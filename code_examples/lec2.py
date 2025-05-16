# Lecture 2: Basic Syntax and Variables
# Demonstrating Python syntax and variable operations

# Variable naming conventions
student_name = "John"    # snake_case (recommended)
studentAge = 20         # camelCase
STUDENT_ID = "12345"    # UPPERCASE for constants

# Multiple assignments
x, y, z = 1, 2, 3
print(f"Multiple assignments: x={x}, y={y}, z={z}")

# Variable swapping
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\nString Operations:")
print(f"Full name: {full_name}")
print(f"Length of name: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Title case: {full_name.title()}")

# Type conversion
number_str = "123"
number_int = int(number_str)
number_float = float(number_str)
print(f"\nType Conversion:")
print(f"String to int: {number_int}")
print(f"String to float: {number_float}")
print(f"Int to string: {str(number_int)}") 