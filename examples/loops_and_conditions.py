"""
Loops and Conditions Example for pyMeow

This example demonstrates control flow structures: for loops, while loops,
and if/else conditions. It showcases how pyMeow makes program flow visible.

When loaded in pyMeow:
- For loops become cyan ForBlocks with editable target and iterable fields
- While loops become magenta WhileBlocks with editable conditions
- If statements become green IfBlocks showing the condition being tested
- Nested structures are visually indented, making the hierarchy clear
- Break and continue statements appear as simple statement blocks

This example helps learners understand:
- How loops repeat code execution
- How conditions control program flow
- The concept of nested structures
- Loop control statements (break, continue)

The visual representation makes it easy to see which code belongs to which
control structure, eliminating common indentation errors.
"""

# Example 1: For loop with range
print("Counting from 0 to 9:")
for i in range(10):
    print(i)

# Example 2: For loop with list
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in the basket:")
for fruit in fruits:
    print("- " + fruit)

# Example 3: While loop with counter
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Blast off!")

# Example 4: If/else conditions
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 5: Nested conditions
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)

# Example 6: Nested loops
print("\nMultiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(i, "x", j, "=", result)

# Example 7: Loop with break
print("\nSearching for number 7:")
for num in range(1, 20):
    print("Checking", num)
    if num == 7:
        print("Found it!")
        break

# Example 8: Loop with continue
print("\nPrinting odd numbers only:")
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# Example 9: While loop with condition check
password = ""
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    # In real code, you'd get input from user
    # For demo, we'll simulate with a hardcoded check
    if password == "secret":
        print("Access granted!")
        break
    else:
        print("Access denied. Try again.")
        attempts = attempts + 1
        # Simulate correct password on third attempt
        if attempts == 2:
            password = "secret"

if attempts == max_attempts and password != "secret":
    print("Too many attempts. Account locked.")