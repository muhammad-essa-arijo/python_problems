"""
Problem: Demonstrate the use of 'sep' and 'end' parameters in the print() function.
"""

print("--- Date Formatter (Using 'sep') ---")
# Using sep to automatically put hyphens between arguments
print("Day", "Month", "Year", sep="-")
print("26", "08", "2026", sep="/")

print("\n--- Loading Bar (Using 'end') ---")
# Using end to prevent print from going to a new line
print("Loading module 1...", end=" [OK] ")
print("Loading module 2...", end=" [OK] ")
print("System Ready!")