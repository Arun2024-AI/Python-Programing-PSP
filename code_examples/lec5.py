# Lecture 5: Functions
# Demonstrating different types of functions in Python

# Basic function
def greet():
    print("Hello, World!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with default parameters
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

# Function with return value
def add_numbers(a, b):
    return a + b

# Function with multiple return values
def get_circle_info(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

# Function with variable arguments
def sum_all(*args):
    return sum(args)

# Function with keyword arguments
def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda function
square = lambda x: x ** 2

# Main execution
if __name__ == "__main__":
    print("Basic Function:")
    greet()
    
    print("\nFunction with Parameters:")
    greet_person("John")
    
    print("\nFunction with Default Parameters:")
    greet_with_title("John")
    greet_with_title("Mary", "Ms.")
    
    print("\nFunction with Return Value:")
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    print("\nFunction with Multiple Return Values:")
    area, circumference = get_circle_info(5)
    print(f"Circle with radius 5:")
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
    
    print("\nFunction with Variable Arguments:")
    total = sum_all(1, 2, 3, 4, 5)
    print(f"Sum of 1, 2, 3, 4, 5 = {total}")
    
    print("\nFunction with Keyword Arguments:")
    print_person_info(name="John", age=25, city="New York")
    
    print("\nLambda Function:")
    print(f"Square of 5: {square(5)}") 