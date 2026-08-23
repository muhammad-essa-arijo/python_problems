"""
Problem: Show the difference between creating an alias of a variable versus copying it in memory.
"""

original_list = ["Apple", "Banana"]

# 1. Aliasing (Sharing same memory)
alias_list = original_list

# 2. Copying (Creating new memory space)
copied_list = original_list.copy()

print(f"Original ID: {id(original_list)}")
print(f"Alias ID:    {id(alias_list)} (Matches original)")
print(f"Copied ID:   {id(copied_list)} (New memory address)\n")

# Changing the original list
original_list.append("Mango")

print("After adding 'Mango' to original list:")
print(f"Original: {original_list}")
print(f"Alias:    {alias_list} (Also changed!)")
print(f"Copied:   {copied_list} (Remains safe!)")