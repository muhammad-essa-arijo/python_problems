"""
Problem: Perform arithmetic calculations directly inside an f-string.
"""

item_name = "Wireless Mouse"
price = 1500
quantity = 3

print("--- Quick Checkout ---")
print(f"Item: {item_name}")
print(f"Price per unit: Rs.{price}")
print(f"Quantity: {quantity}")

# Doing the math directly inside the f-string!
print(f"Total Amount Payable: Rs.{price * quantity}")