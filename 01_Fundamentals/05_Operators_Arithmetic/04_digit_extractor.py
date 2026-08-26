"""
Problem: Extract and remove the last digit of a number using % and //.
"""

number = 549

print(f"Original Number: {number}")

# Get the last digit using Modulo 10
last_digit = number % 10
print(f"Extracted Last Digit: {last_digit}")

# Remove the last digit using Floor Division by 10
number_without_last = number // 10
print(f"Number after removing last digit: {number_without_last}")