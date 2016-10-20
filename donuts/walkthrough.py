"""
Walkthrough: Selling flags to buy beer
"""


# prompt for dollar to pound exchange
pounds_per_dollar = input("Current dollar-to-pound exchange rate: ")
pounds_per_dollar = float(pounds_per_dollar)

# prompt for number of flags to sell
num_flags = input("How many flags did you sell? ")
num_flags = int(num_flags)

# create variables for fixed values (cost flag, cost of pint)
pounds_per_pint = 3.79
dollars_per_flag = 3

# calculate how much a flag costs in pounds
pounds_per_flag = dollars_per_flag * pounds_per_dollar

# calculate how many pounds I'll have after selling them all
revenue = num_flags * pounds_per_flag

# calculate number beers I can buy with that amount of money
num_pints = revenue / pounds_per_pint
num_pints = int(num_pints)

# print out number of pints
print("You can afford", num_pints, "pints of beer!")
