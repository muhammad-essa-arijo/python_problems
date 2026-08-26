"""
Problem: Calculate Body Mass Index (BMI) using the exponentiation (**) operator.
"""

weight_kg = 80
height_meters = 1.8

# Formula for BMI: weight / (height squared)
# Using ** 2 to square the height
bmi = weight_kg / (height_meters ** 2)

print("--- BMI Calculator ---")
print(f"Weight: {weight_kg} kg")
print(f"Height: {height_meters} m")
# Rounding to 2 decimal places for a cleaner output
print(f"Your BMI is: {round(bmi, 2)}")