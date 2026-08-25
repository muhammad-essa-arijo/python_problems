"""
Problem: Convert a string containing a decimal number into an integer correctly.
"""

price_str = "99.99"

print(f"Original String: '{price_str}'")

# direct_int = int(price_str)  # THIS WILL CAUSE A VALUE ERROR!

# Correct way: First cast to float, then cast to int
price_float = float(price_str)
price_int = int(price_float)

print(f"Converted to Float: {price_float}")
print(f"Final Integer (decimals truncated): {price_int}")