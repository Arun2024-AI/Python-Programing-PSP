# Lecture 4: Control Structures
# Demonstrating if-else, loops, and other control structures

# If-else statements
age = 18
print("If-else Example:")
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-elif-else
score = 85
print("\nIf-elif-else Example:")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# For loop
print("\nFor Loop Examples:")
# Range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# List iteration
fruits = ["apple", "banana", "cherry"]
print("\nIterating through list:")
for fruit in fruits:
    print(fruit)

# While loop
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# Break and Continue
print("\nBreak Example:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\nContinue Example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# Nested loops
print("\nNested Loops Example:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Try-except
print("\nTry-except Example:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This will always execute") 