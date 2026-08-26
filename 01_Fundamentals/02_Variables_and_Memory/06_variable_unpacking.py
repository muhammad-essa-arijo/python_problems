"""
Problem: Demonstrate variable unpacking, including extended unpacking using the * operator.
"""

# 1. Standard Unpacking
student_info = ["Essa", 18, "Software Engineering"]
name, age, major = student_info

print("--- Standard Unpacking ---")
print(f"Name: {name} | Age: {age} | Major: {major}\n")

# 2. Extended Unpacking (Using *)
# What if we have a list of marks, but only want the first and last?
marks = [85, 90, 78, 92, 88]
first_subject, *middle_subjects, last_subject = marks

print("--- Extended Unpacking ---")
print(f"First Subject: {first_subject}")
print(f"Middle Subjects (Packed into a list): {middle_subjects}")
print(f"Last Subject: {last_subject}")