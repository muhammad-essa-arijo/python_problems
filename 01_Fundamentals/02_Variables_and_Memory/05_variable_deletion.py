"""
Problem: Create a variable, print its memory address, delete it using 'del', and handle the resulting error.
"""

secret_code = 998877
print(f"Variable exists! Value: {secret_code} | Memory: {id(secret_code)}")

print("Deleting the variable from memory...")
del secret_code

# Trying to access the deleted variable will crash the program, 
# so we use a try-except block to catch it gracefully.
try:
    print(secret_code)
except NameError:
    print("Error: The variable 'secret_code' no longer exists in memory!")