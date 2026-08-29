"""
Problem: Swap the values of two variables using the Bitwise XOR (^) operator.
"""

a = 10
b = 25

print("--- XOR Variable Swap ---")
print(f"Before Swapping: a = {a}, b = {b}")

# Step-by-step XOR swapping logic
a = a ^ b  # a now holds the XOR of both
b = a ^ b  # b becomes the original value of a
a = a ^ b  # a becomes the original value of b

print(f"After Swapping:  a = {a}, b = {b}")