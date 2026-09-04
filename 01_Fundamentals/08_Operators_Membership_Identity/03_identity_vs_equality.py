"""
Problem: Demonstrate the difference between '==' (Value Equality) and 'is' (Memory Identity).
"""

# Two separate lists with the EXACT same values
list_A = [1, 2, 3]
list_B = [1, 2, 3]
list_C = list_A  # list_C is just an alias pointing to list_A's memory

print("--- Equality (==) vs Identity (is) ---")

# Equality (==) checks if the contents are the same
print(f"Does list_A have the same values as list_B? {list_A == list_B}")

# Identity (is) checks if they are the EXACT SAME object in memory
print(f"Are list_A and list_B the exact same object in memory? {list_A is list_B}")

# Checking the alias
print(f"Are list_A and list_C the exact same object in memory? {list_A is list_C}")