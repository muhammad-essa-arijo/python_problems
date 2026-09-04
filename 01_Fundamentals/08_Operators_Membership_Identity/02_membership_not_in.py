"""
Problem: Use the 'not in' operator to check if a username is available.
"""

taken_usernames = ["admin", "root", "essa99", "guest"]
new_user = "web_coder"

print("--- Username Availability Checker ---")
print(f"Taken Usernames: {taken_usernames}")
print(f"Requested Username: {new_user}\n")

# The 'not in' operator returns True if the item is ABSENT from the list
is_available = new_user not in taken_usernames

if is_available:
    print(f"Success: '{new_user}' is available!")
else:
    print(f"Error: '{new_user}' is already taken.")