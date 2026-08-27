"""
Problem: Simulate a logical XOR using the '!=' (not equal) relational operator.
"""

# Scenario: We can either get a Tea or a Coffee with our meal, but NOT both!
wants_tea = True
wants_coffee = True

print("--- Beverage Selection ---")

# This evaluates to True ONLY if they are different (one True, one False)
valid_selection = wants_tea != wants_coffee

print(f"Tea selected: {wants_tea}")
print(f"Coffee selected: {wants_coffee}")
print(f"\nIs the order valid (only one selected)? {valid_selection}")