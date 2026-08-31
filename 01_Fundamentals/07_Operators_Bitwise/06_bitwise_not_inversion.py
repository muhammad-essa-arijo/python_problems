"""
Problem: Demonstrate the Bitwise NOT (~) operator and how it applies 2's complement.
"""

number = 5

# Bitwise NOT flips all bits
inverted = ~number

print("--- Bitwise NOT Operator ---")
print(f"Original Number: {number}")
# Formula for bitwise NOT in Python is -(n + 1)
print(f"Inverted Number (~{number}): {inverted}")