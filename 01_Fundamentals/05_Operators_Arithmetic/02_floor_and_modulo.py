"""
Problem: Convert total minutes into hours and remaining minutes using floor division (//) and modulo (%).
"""

total_minutes = 135

# Floor Division (//) gives the exact hours without decimals
hours = total_minutes // 60

# Modulo (%) gives the remainder, which are the leftover minutes
remaining_minutes = total_minutes % 60

print(f"Total Minutes: {total_minutes}")
print(f"Converted Time: {hours} Hours and {remaining_minutes} Minutes")