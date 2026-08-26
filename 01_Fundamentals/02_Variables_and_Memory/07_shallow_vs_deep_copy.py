"""
Problem: Show the difference between Shallow Copy and Deep Copy when dealing with nested lists.
"""
import copy

print("--- Shallow Copy Warning ---")
original_matrix = [[1, 2], [3, 4]]
shallow_copied = original_matrix.copy()

# Modifying the inner list of the shallow copy
shallow_copied[0][0] = 99
print(f"Original after Shallow Copy change: {original_matrix} (It accidentally changed!)")
print(f"Shallow Copy: {shallow_copied}\n")

print("--- Deep Copy Solution ---")
# Resetting the matrix
original_matrix = [[1, 2], [3, 4]]
deep_copied = copy.deepcopy(original_matrix)

# Modifying the inner list of the deep copy
deep_copied[0][0] = 99
print(f"Original after Deep Copy change: {original_matrix} (Remains safe!)")
print(f"Deep Copy: {deep_copied}")