"""
Problem: Use the 'or' operator to check if a person is allowed inside the campus.
"""

has_k25sw_id = True
has_visitor_pass = False

print("--- Campus Security Gate ---")
# Only one condition needs to be True for entry
can_enter = has_k25sw_id or has_visitor_pass

print(f"Student ID Present: {has_k25sw_id}")
print(f"Visitor Pass Present: {has_visitor_pass}")
print(f"\nAccess Granted: {can_enter}")