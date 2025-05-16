# Lecture 3: Data Types
# Demonstrating different data types in Python

# Numbers
integer_num = 42
float_num = 3.14
complex_num = 1 + 2j
print("Numbers:")
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# Strings
single_quoted = 'Hello'
double_quoted = "World"
multi_line = '''This is a
multi-line string'''
print("\nStrings:")
print(f"Single quoted: {single_quoted}")
print(f"Double quoted: {double_quoted}")
print(f"Multi-line: {multi_line}")

# Lists
my_list = [1, 2, 3, "Python", True]
print("\nList Operations:")
print(f"Original list: {my_list}")
my_list.append(4)
print(f"After append: {my_list}")
print(f"List slicing: {my_list[1:3]}")

# Tuples
my_tuple = (1, 2, 3, "Python")
print("\nTuple:")
print(f"Tuple: {my_tuple}")
print(f"Tuple is immutable, cannot be modified")

# Dictionaries
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print("\nDictionary:")
print(f"Dictionary: {my_dict}")
print(f"Accessing value: {my_dict['name']}")

# Sets
my_set = {1, 2, 3, 3, 4, 4, 5}
print("\nSet:")
print(f"Set (removes duplicates): {my_set}")
my_set.add(6)
print(f"After adding element: {my_set}")

# Boolean
is_true = True
is_false = False
print("\nBoolean:")
print(f"True: {is_true}")
print(f"False: {is_false}")
print(f"Boolean operations: {True and False}")
print(f"Boolean operations: {True or False}")
print(f"Boolean operations: {not True}") 