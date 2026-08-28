"""
Problem: Combine different system permissions using the Bitwise OR (|) operator.
"""

# Binary Flags
READ = 0b100    # 4 in decimal
WRITE = 0b010   # 2 in decimal
EXECUTE = 0b001 # 1 in decimal

print("--- System Permissions ---")
print(f"Read: {bin(READ)} | Write: {bin(WRITE)} | Execute: {bin(EXECUTE)}")

# Combine Read and Write permissions for a user
user_permission = READ | WRITE

print(f"\nCombined Permission (Read + Write): {bin(user_permission)}")
print(f"Decimal Value: {user_permission}")