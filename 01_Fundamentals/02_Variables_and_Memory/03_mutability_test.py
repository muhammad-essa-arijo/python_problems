"""
Problem: Demonstrate the difference between mutable (list) and immutable (string) data types in memory when modified.
"""

# Testing Immutable (String)
my_text = "Hello"
print(f"Original String: '{my_text}' | Address: {id(my_text)}")

my_text = my_text + " World"
print(f"Updated String: '{my_text}' | Address: {id(my_text)} -> (Address Changed!)\n")

# Testing Mutable (List)
my_list = [1, 2, 3]
print(f"Original List: {my_list} | Address: {id(my_list)}")

my_list.append(4)
print(f"Updated List: {my_list} | Address: {id(my_list)} -> (Address Kept Same!)")