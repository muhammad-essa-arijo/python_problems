"""
Problem: Demonstrate Python's integer caching by comparing memory addresses of variables holding the same small number.
"""

a = 100
b = 100

print(f"Value of a: {a} | Memory Address: {id(a)}")
print(f"Value of b: {b} | Memory Address: {id(b)}")

# Use 'is' operator to check if they point to the exact same memory location
if a is b:
    print("\nResult: Both variables point to the SAME memory address!")
else:
    print("\nResult: Variables point to DIFFERENT memory addresses.")