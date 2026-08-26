"""
Problem: Use the modulo operator (%) to determine if a number is completely divisible by 2 (Even).
"""

number = 42

# Any number modulo 2 will result in 0 if it's even, and 1 if it's odd.
remainder = number % 2

print(f"The number is: {number}")
print(f"Remainder when divided by 2 is: {remainder}")

# Using a simple check (returns True or False)
is_even = (remainder == 0)

print(f"Is the number even? {is_even}")