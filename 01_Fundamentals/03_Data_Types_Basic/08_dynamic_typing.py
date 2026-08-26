"""
Problem: Show how a single variable can hold different data types at different times.
"""

# Starting with a String
my_variable = "Hello, World!"
print(f"Value: {my_variable} | Type: {type(my_variable)}")

# Changing the exact same variable to an Integer
my_variable = 100
print(f"Value: {my_variable} | Type: {type(my_variable)}")

# Changing it to a Float
my_variable = 99.99
print(f"Value: {my_variable} | Type: {type(my_variable)}")