"""
Problem: Calculate total marks and percentage for three university subjects.
"""

# Marks obtained out of 100 for each subject
qr_marks = 85
dsa_marks = 89
database_marks = 92

total_obtained = qr_marks + dsa_marks + database_marks
max_total_marks = 300  # 100 for each of the 3 subjects

# Percentage formula: (Obtained / Total) * 100
percentage = (total_obtained / max_total_marks) * 100

print("--- MUET SZAB Campus Results ---")
print(f"Total Marks Obtained: {total_obtained} / {max_total_marks}")
# Using round() to keep it to 2 decimal places
print(f"Final Percentage: {round(percentage, 2)}%")