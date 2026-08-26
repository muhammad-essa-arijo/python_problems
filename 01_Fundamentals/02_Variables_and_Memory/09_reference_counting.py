"""
Problem: Use the sys module to check the reference count of a variable in memory.
"""
import sys

# Create a unique list in memory
my_data = ["Python", "DSA", "Oracle"]

# sys.getrefcount() returns the number of references pointing to this memory block.
# (It always returns actual count + 1 because passing it to the function creates a temporary reference)
print(f"Initial Reference Count: {sys.getrefcount(my_data) - 1}")

# Create an alias (another variable pointing to the same memory)
alias_data = my_data
print(f"Count after creating an alias: {sys.getrefcount(my_data) - 1}")

# Delete the alias
del alias_data
print(f"Count after deleting the alias: {sys.getrefcount(my_data) - 1}")