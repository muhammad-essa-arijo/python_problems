"""
Problem: Use a relational operator to check if a password string meets the minimum length.
"""

user_password = "mysecretcode"
min_required_length = 8

password_length = len(user_password)

# Check if the length is greater than or equal to 8
is_secure = password_length >= min_required_length

print("--- Password Security Check ---")
print(f"Your password is {password_length} characters long.")
print(f"Is password secure (8+ characters)? {is_secure}")