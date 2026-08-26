"""
Problem: Calculate net freelance earnings after a 20% platform fee and convert from USD to PKR.
"""

project_price_usd = 150  # $150 project on Fiverr
platform_fee_percent = 20
exchange_rate_pkr = 278.50

# Calculate the fee amount (Percentage formula: (percent / 100) * total)
fee_amount = (platform_fee_percent / 100) * project_price_usd

# Calculate net earnings in USD
net_usd = project_price_usd - fee_amount

# Convert to PKR
net_pkr = net_usd * exchange_rate_pkr

print(f"Total Project Value: ${project_price_usd}")
print(f"Platform Fee (20%): -${fee_amount}")
print(f"Net Earnings: ${net_usd}")
print(f"Total in PKR: Rs. {net_pkr}")