"""
Problem: Define integers using binary, octal, and hexadecimal literals and convert them.
"""

# Defining numbers in different bases (Python automatically stores them as normal integers)
binary_num = 0b1010       # Starts with 0b (10 in decimal)
octal_num = 0o12          # Starts with 0o (10 in decimal)
hex_num = 0xA             # Starts with 0x (10 in decimal)

print("--- Different Bases to Decimal ---")
print(f"Binary 0b1010 is Decimal: {binary_num}")
print(f"Octal 0o12 is Decimal: {octal_num}")
print(f"Hex 0xA is Decimal: {hex_num}\n")

# Converting a normal integer back to different bases
normal_num = 255
print("--- Decimal to Different Bases ---")
print(f"255 in Binary: {bin(normal_num)}")
print(f"255 in Octal: {oct(normal_num)}")  # FIXED: Changed octal() to oct()
print(f"255 in Hex: {hex(normal_num)}")