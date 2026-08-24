"""
Problem: Demonstrate basic Type Hinting (Annotations) for variables.
"""

# Adding type hints using a colon (:)
# This tells other developers what type of data this variable SHOULD hold
student_name: str = "Essa"
age: int = 18
is_active: bool = True
gpa: float = 3.9

print("--- Type Hinted Variables ---")
print(f"Name: {student_name}")
print(f"Age: {age}")
print(f"Active: {is_active}")
print(f"GPA: {gpa}\n")

# Note: Python is dynamically typed. It won't throw an error if we do this:
# age = "Eighteen"
# But our code editor (like VS Code) will warn us that we are breaking the hint!