"""
Problem: Combine relational and logical operators for a library borrowing system.
"""

books_currently_borrowed = 2
max_limit = 3
has_overdue_fines = False

print("--- Library Loan System ---")

# Check if borrowed books are less than limit AND they don't have fines
can_borrow_more = (books_currently_borrowed < max_limit) and not has_overdue_fines

print(f"Books Borrowed: {books_currently_borrowed}/{max_limit}")
print(f"Has Fines: {has_overdue_fines}")
print(f"\nEligible to borrow new book: {can_borrow_more}")