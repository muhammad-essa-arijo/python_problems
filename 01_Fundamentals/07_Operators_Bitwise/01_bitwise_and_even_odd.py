"""
Problem: Check if a number is even or odd using the Bitwise AND (&) operator.
"""

number = 45

# Binary of 45 ends with 1. 
# 45 & 1 compares the last bit.
is_odd = (number & 1) == 1

print("--- Fast Even/Odd Checker ---")
print(f"Number to check: {number}")
print(f"Is the number Odd? {is_odd}")

if is_odd:
    print("Result: The number is ODD.")
else:
    print("Result: The number is EVEN.")