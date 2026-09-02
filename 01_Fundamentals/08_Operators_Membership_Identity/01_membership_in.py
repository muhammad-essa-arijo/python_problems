"""
Problem: Use the 'in' operator to check if a specific subject is in a list of courses.
"""

semester_courses = ["OOP", "DSA", "Calculus", "Database"]
search_course = "DSA"

print("--- Course Search System ---")
print(f"Available Courses: {semester_courses}")
print(f"Looking for: {search_course}\n")

# The 'in' operator returns True if the item exists in the list
is_enrolled = search_course in semester_courses

print(f"Is {search_course} in the semester list? {is_enrolled}")