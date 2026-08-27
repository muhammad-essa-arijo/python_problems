"""
Problem: Demonstrate Python's ability to chain relational operators to check ranges.
"""

temperature = 25

print("--- Weather Range Check ---")
print(f"Current Temperature: {temperature}°C")

# Standard way: (temperature >= 20) and (temperature <= 30)
# Pythonic Chained way:
is_pleasant = 20 <= temperature <= 30

print(f"Is the weather pleasant (between 20 and 30)? {is_pleasant}")