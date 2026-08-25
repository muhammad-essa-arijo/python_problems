"""
Problem: Take birth year as string input, cast it to int, and calculate current age.
"""

# input() always returns a string
birth_year_str = input("Enter your birth year (e.g., 2005): ")

print(f"\nBefore casting: '{birth_year_str}' is {type(birth_year_str)}")

# Explicitly casting string to integer
birth_year_int = int(birth_year_str)
current_year = 2026
age = current_year - birth_year_int

print(f"After casting: {birth_year_int} is {type(birth_year_int)}")
print(f"You are {age} years old.")