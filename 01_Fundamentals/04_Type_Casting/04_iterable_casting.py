"""
Problem: Use type casting to remove duplicates from a list by converting it to a set.
"""

# A list with duplicate numbers
student_marks = [85, 90, 85, 75, 90, 100]
print(f"Original List: {student_marks} | Type: {type(student_marks)}")

# Cast List to Set (Sets automatically remove duplicates!)
unique_marks_set = set(student_marks)
print(f"After casting to Set: {unique_marks_set} | Type: {type(unique_marks_set)}")

# Cast back to a Tuple (if we want the data to be immutable/unchangeable)
final_marks_tuple = tuple(unique_marks_set)
print(f"Final Tuple: {final_marks_tuple} | Type: {type(final_marks_tuple)}")