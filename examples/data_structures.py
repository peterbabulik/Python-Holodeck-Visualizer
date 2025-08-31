"""
Data Structures Example for pyMeow

This example demonstrates Python's built-in data structures: lists, dictionaries,
sets, tuples, and advanced features like list comprehensions.

When loaded in pyMeow:
- List operations appear as assignment blocks with list literals
- Dictionary operations show key-value pairs clearly
- List comprehensions are preserved in their compact form
- Loops iterating over data structures are visually clear
- The relationships between data and operations are evident

This example helps learners understand:
- Different types of data structures and their uses
- How to create and manipulate collections
- Iteration over various data structures
- List comprehensions as a powerful Python feature
- When to use each type of data structure

The visual blocks help distinguish between different data types
and make complex operations like comprehensions less intimidating.
"""

# === Lists ===
print("=== Working with Lists ===")

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed_list = [42, "hello", 3.14, True]
empty_list = []

# List operations
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.insert(0, "mango")
print("Fruits:", fruits)

# Accessing list elements
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)

# List slicing
some_fruits = fruits[1:3]
print("Some fruits:", some_fruits)

# List iteration
print("All fruits:")
for fruit in fruits:
    print("- " + fruit)

# List comprehension - squares of numbers
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# List comprehension with condition - even numbers only
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)

# Nested list comprehension - multiplication table
mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table:")
for row in mult_table:
    print(row)


# === Dictionaries ===
print("\n=== Working with Dictionaries ===")

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Dictionary operations
person["email"] = "alice@example.com"
person["age"] = 26
print("Person info:", person)

# Accessing dictionary values
name = person["name"]
age = person.get("age", 0)  # with default value
print("Name:", name, "Age:", age)

# Dictionary iteration
print("Person details:")
for key in person:
    value = person[key]
    print(key + ":", value)

# Dictionary comprehension - word lengths
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)

# Nested dictionary
students = {
    "Alice": {"age": 20, "grade": "A", "subjects": ["Math", "Science"]},
    "Bob": {"age": 21, "grade": "B", "subjects": ["English", "History"]},
    "Charlie": {"age": 19, "grade": "A", "subjects": ["Math", "Art"]}
}

# Accessing nested dictionary
for student_name in students:
    student_data = students[student_name]
    print(student_name + "'s grade:", student_data["grade"])


# === Sets ===
print("\n=== Working with Sets ===")

# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
another_set = {4, 5, 6, 7, 8}

# Set operations
unique_numbers.add(6)
unique_numbers.remove(1)
print("Modified set:", unique_numbers)

# Set operations - union, intersection, difference
union_set = unique_numbers | another_set
intersection_set = unique_numbers & another_set
difference_set = unique_numbers - another_set

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

# Set comprehension - unique squares
unique_squares = {x**2 for x in range(-5, 6)}
print("Unique squares:", unique_squares)


# === Tuples ===
print("\n=== Working with Tuples ===")

# Creating tuples (immutable)
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item = (42,)  # Note the comma for single item tuple

# Tuple unpacking
x, y = coordinates
print("X:", x, "Y:", y)

# Named tuple-like usage with multiple return values
def get_min_max(numbers):
    """Return minimum and maximum as a tuple."""
    if len(numbers) == 0:
        return (None, None)
    return (min(numbers), max(numbers))

test_nums = [5, 2, 8, 1, 9, 3]
min_val, max_val = get_min_max(test_nums)
print("Min:", min_val, "Max:", max_val)


# === Advanced Examples ===
print("\n=== Advanced Data Structure Examples ===")

# List of dictionaries
inventory = [
    {"item": "apple", "quantity": 50, "price": 0.5},
    {"item": "banana", "quantity": 30, "price": 0.3},
    {"item": "orange", "quantity": 20, "price": 0.6}
]

# Calculate total value
total_value = 0
for item in inventory:
    value = item["quantity"] * item["price"]
    total_value = total_value + value
    print(item["item"] + " value:", value)
print("Total inventory value:", total_value)

# Dictionary of lists
class_roster = {
    "Math": ["Alice", "Bob", "Charlie"],
    "Science": ["Alice", "Diana", "Eve"],
    "English": ["Bob", "Charlie", "Frank"]
}

# Find students taking multiple subjects
all_students = set()
for subject in class_roster:
    students = class_roster[subject]
    for student in students:
        all_students.add(student)

print("All unique students:", all_students)

# Nested list comprehension with filtering
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row if num % 2 == 0]
print("Even numbers from matrix:", flattened)

# Dictionary with list values - grouping
grades = [85, 92, 78, 95, 88, 73, 82, 90, 87, 91]
grade_groups = {
    "A": [g for g in grades if g >= 90],
    "B": [g for g in grades if 80 <= g < 90],
    "C": [g for g in grades if 70 <= g < 80]
}

for letter in grade_groups:
    group = grade_groups[letter]
    print("Grade " + letter + ":", group)

# Combining multiple data structures
# Create a simple database-like structure
database = {
    "users": [
        {"id": 1, "name": "Alice", "posts": [101, 102]},
        {"id": 2, "name": "Bob", "posts": [103]},
        {"id": 3, "name": "Charlie", "posts": [104, 105, 106]}
    ],
    "posts": {
        101: {"title": "Hello World", "likes": 5},
        102: {"title": "Python Tips", "likes": 12},
        103: {"title": "Learning PyMeow", "likes": 8},
        104: {"title": "Data Structures", "likes": 15},
        105: {"title": "Visual Programming", "likes": 10},
        106: {"title": "Code Blocks", "likes": 7}
    }
}

# Query the database structure
print("\n=== User Post Summary ===")
for user in database["users"]:
    total_likes = 0
    print(user["name"] + "'s posts:")
    for post_id in user["posts"]:
        post = database["posts"][post_id]
        print("  -", post["title"], "(" + str(post["likes"]) + " likes)")
        total_likes = total_likes + post["likes"]
    print("  Total likes:", total_likes)