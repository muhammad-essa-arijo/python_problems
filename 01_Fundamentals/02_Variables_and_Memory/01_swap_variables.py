"""
Problem Statement: Take two inputs, store them in variables, and swap their values without using a third variable. Print before and after.
"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
