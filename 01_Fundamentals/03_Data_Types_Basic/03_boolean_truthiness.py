"""
Problem: Demonstrate the concept of 'truthiness' by converting various values to booleans.
"""

# Falsy Values (Evaluate to False)
print("--- Falsy Values ---")
print(f"Integer 0 is: {bool(0)}")
print(f"Empty String \"\" is: {bool('')}")
print(f"Float 0.0 is: {bool(0.0)}")
print(f"None is: {bool(None)}")

# Truthy Values (Evaluate to True)
print("\n--- Truthy Values ---")
print(f"Integer 1 (or any number) is: {bool(1)}")
print(f"Negative Number -5 is: {bool(-5)}")
print(f"Non-empty String 'Essa' is: {bool('Essa')}")
print(f"A space string ' ' is: {bool(' ')}")