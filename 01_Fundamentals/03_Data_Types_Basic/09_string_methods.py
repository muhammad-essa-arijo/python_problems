"""
Problem: Create a string variable and use basic methods to change its format.
"""

message = "python programming is fun!"

# .upper() makes everything uppercase
print(f"Uppercase: {message.upper()}")

# .title() capitalizes the first letter of each word
print(f"Title Case: {message.title()}")

# .replace() swaps out specific words
new_message = message.replace("fun", "awesome")
print(f"Replaced Word: {new_message}")