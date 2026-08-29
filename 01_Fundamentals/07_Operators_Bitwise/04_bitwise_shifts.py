"""
Problem: Multiply and divide a number by 2 using Bitwise Left Shift (<<) and Right Shift (>>).
"""

num = 16

print("--- Fast Math with Bitwise Shifts ---")
print(f"Original Number: {num}")

# Left Shift by 1 (Multiplies by 2)
multiplied = num << 1
print(f"Left Shift by 1 (16 * 2): {multiplied}")

# Right Shift by 1 (Divides by 2)
divided = num >> 1
print(f"Right Shift by 1 (16 / 2): {divided}")