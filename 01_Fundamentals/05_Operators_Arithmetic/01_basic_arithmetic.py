"""
Problem: Use basic arithmetic operators to calculate the total cost, discount, and final price of items.
"""

item1_price = 1500
item2_price = 850
quantity = 2

# Addition and Multiplication
subtotal = item1_price + (item2_price * quantity)

# Subtraction
discount = 200
final_price = subtotal - discount

# Division (Always returns a float, e.g., 5.0)
split_between_2 = final_price / 2

print("--- Shopping Receipt ---")
print(f"Subtotal: Rs. {subtotal}")
print(f"Discount: Rs. {discount}")
print(f"Final Price: Rs. {final_price}")
print(f"Half Contribution: Rs. {split_between_2}")