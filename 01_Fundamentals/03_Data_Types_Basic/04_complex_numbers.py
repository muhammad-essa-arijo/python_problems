"""
Problem: Create complex numbers, perform basic addition, and extract real and imaginary parts.
"""

# Creating complex numbers
num1 = 4 + 3j
num2 = 2 - 1j

# Addition of complex numbers
result = num1 + num2

print(f"First Complex Number: {num1}")
print(f"Second Complex Number: {num2}")
print(f"Sum: {result}\n")

# Extracting Real and Imaginary parts
print("--- Breakdown of First Number ---")
print(f"Real Part: {num1.real}")
print(f"Imaginary Part: {num1.imag}")