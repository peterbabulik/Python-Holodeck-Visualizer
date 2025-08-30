"""
Fibonacci Sequence Example for pyMeow

This example demonstrates recursive functions through the classic Fibonacci
sequence implementation, showing both recursive and iterative approaches.

When loaded in pyMeow:
- Recursive function calls are clearly visible as nested blocks
- The base case and recursive case are distinct in the if/else structure
- Return statements show how values bubble up through recursion
- The iterative version shows loop-based alternative approach
- Function calls within return statements are preserved

This example helps learners understand:
- What recursion is and how it works
- The importance of base cases in recursion
- How recursive calls build up and resolve
- Comparing recursive vs iterative solutions
- Performance considerations in algorithm design

The visual blocks make the abstract concept of recursion concrete by
showing the structure of recursive calls and how they relate to each other.
"""

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Each number is the sum of the two preceding ones.
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration.
    
    This is more efficient than recursion for large values of n.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Start with first two Fibonacci numbers
        prev_prev = 0
        prev = 1
        
        # Calculate each Fibonacci number up to n
        for i in range(2, n + 1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        
        return prev


def fibonacci_sequence(count):
    """
    Generate a list of the first 'count' Fibonacci numbers.
    """
    sequence = []
    for i in range(count):
        num = fibonacci_iterative(i)
        sequence.append(num)
    return sequence


def fibonacci_with_memoization(n, memo=None):
    """
    Calculate Fibonacci with memoization to improve performance.
    
    Memoization stores previously calculated values to avoid
    redundant recursive calls.
    """
    if memo is None:
        memo = {}
    
    # Check if we've already calculated this value
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        # Recursive case with memoization
        result = fibonacci_with_memoization(n - 1, memo) + fibonacci_with_memoization(n - 2, memo)
    
    # Store the result for future use
    memo[n] = result
    return result


def is_fibonacci_number(num):
    """
    Check if a given number is part of the Fibonacci sequence.
    """
    if num < 0:
        return False
    
    # Generate Fibonacci numbers until we reach or exceed num
    a = 0
    b = 1
    
    if num == a or num == b:
        return True
    
    while b < num:
        c = a + b
        if c == num:
            return True
        a = b
        b = c
    
    return False


def fibonacci_ratio(n):
    """
    Calculate the ratio between consecutive Fibonacci numbers.
    
    As n increases, this ratio approaches the golden ratio (φ ≈ 1.618).
    """
    if n <= 1:
        return 0
    
    fib_n = fibonacci_iterative(n)
    fib_n_minus_1 = fibonacci_iterative(n - 1)
    
    if fib_n_minus_1 == 0:
        return 0
    
    ratio = fib_n / fib_n_minus_1
    return ratio


# === Example Usage ===

print("=== Fibonacci Sequence Examples ===\n")

# Example 1: Calculate individual Fibonacci numbers
print("Individual Fibonacci numbers:")
for i in range(10):
    fib_recursive = fibonacci_recursive(i)
    fib_iterative_result = fibonacci_iterative(i)
    print("F(" + str(i) + ") =", fib_recursive, "(recursive),", fib_iterative_result, "(iterative)")

# Example 2: Generate a sequence
print("\nFirst 15 Fibonacci numbers:")
sequence = fibonacci_sequence(15)
print(sequence)

# Example 3: Check if numbers are Fibonacci
print("\nChecking if numbers are in Fibonacci sequence:")
test_numbers = [0, 1, 4, 5, 7, 8, 13, 20, 21]
for num in test_numbers:
    if is_fibonacci_number(num):
        print(str(num) + " is a Fibonacci number")
    else:
        print(str(num) + " is NOT a Fibonacci number")

# Example 4: Golden ratio approximation
print("\nFibonacci ratios approaching golden ratio:")
print("Golden ratio ≈ 1.618033988749...")
for n in [5, 10, 15, 20, 25]:
    ratio = fibonacci_ratio(n)
    print("F(" + str(n) + ")/F(" + str(n-1) + ") =", ratio)

# Example 5: Performance comparison
print("\nComparing performance with memoization:")
test_n = 35

import time

# Measure recursive without memoization (will be slow for large n)
start_time = time.time()
result_recursive = fibonacci_recursive(test_n)
time_recursive = time.time() - start_time
print("Recursive F(" + str(test_n) + ") =", result_recursive)
print("Time:", time_recursive, "seconds")

# Measure with memoization
start_time = time.time()
result_memo = fibonacci_with_memoization(test_n)
time_memo = time.time() - start_time
print("With memoization F(" + str(test_n) + ") =", result_memo)
print("Time:", time_memo, "seconds")

# Measure iterative
start_time = time.time()
result_iterative = fibonacci_iterative(test_n)
time_iterative = time.time() - start_time
print("Iterative F(" + str(test_n) + ") =", result_iterative)
print("Time:", time_iterative, "seconds")

print("\nSpeed improvement with memoization:", round(time_recursive / time_memo, 2), "times faster")
print("Speed improvement with iteration:", round(time_recursive / time_iterative, 2), "times faster")

# Example 6: Fibonacci in nature
print("\n=== Fibonacci in Nature ===")
print("The Fibonacci sequence appears in many natural phenomena:")
print("- Spiral shells follow Fibonacci patterns")
print("- Flower petals often come in Fibonacci numbers (3, 5, 8, 13, 21...)")
print("- Tree branches follow Fibonacci patterns")
print("- The golden ratio derived from Fibonacci appears in art and architecture")