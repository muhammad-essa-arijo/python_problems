"""
Problem: Demonstrate the use of NoneType and how to check for None correctly.
"""

# Assigning None to a variable (means no value yet)
user_email = None

print(f"Value: {user_email} | Type: {type(user_email)}")

#  checking for None using 'is' or 'is not'
if user_email is None:
    print("Email is missing! Please update your profile.")
else:
    print(f"Sending email to: {user_email}")

# Updating the value later
user_email = "essa@example.com"
print(f"Updated Email: {user_email}")