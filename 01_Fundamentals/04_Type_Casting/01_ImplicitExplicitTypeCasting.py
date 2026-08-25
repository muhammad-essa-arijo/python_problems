"""
Problem: Demonstrate the difference between Implicit and Explicit type conversion.
"""

# Implicit Casting (Done automatically)
num_int = 10
num_float = 2.5
result_implicit = num_int + num_float

print("--- Implicit Casting ---")
print(f"num_int type: {type(num_int)}")
print(f"num_float type: {type(num_float)}")
print(f"Result: {result_implicit} | Result Type: {type(result_implicit)}\n")

# Explicit Casting (We do it manually)
price = 500
message = "The total price is Rs. " + str(price)  # Explicitly casting int to str

print("--- Explicit Casting ---")
print(message)