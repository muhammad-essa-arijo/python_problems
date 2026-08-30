"""
Problem: Find the single non-repeating number in a list using Bitwise XOR (^).
"""

# The array: 4 and 2 repeat, but 7 is unique
numbers = [4, 2, 7, 2, 4]

unique_num = 0

# XORing all numbers together
for num in numbers:
    unique_num = unique_num ^ num

print("--- Find the Unique Number ---")
print(f"List of numbers: {numbers}")
print(f"The unique number is: {unique_num}")
# Explanation: 4^4 = 0, 2^2 = 0. So, 0 ^ 0 ^ 7 = 7.