"""
Walkthrough: Create a tip calculator
"""

#prompt the user for meal subtotal
subtotal = input("Meal subtotal: ")
subtotal = float(subtotal)

# prompt the user for tip %
tip_pct = input("Tip %: ")

# convert % value to decimal value
tip_pct = float(tip_pct) * 0.01

#calculate the tip amount
tip = subtotal * tip_pct

# print tip amount
print("Tip:",tip)
