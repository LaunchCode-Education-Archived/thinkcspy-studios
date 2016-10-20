"""
Studio: Donuts
"""

# program parameters
special_desc = "Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Berries Oops All Berries"
suggested_price = "4.35"
tax_rate = 0.05

# print info, and get input
print("Welcome to the Loop Hole!")
print("Today's Manager's Special is:")
print(special_desc)

num_donuts = float(input("How many would you like?"))
cost_per = float(input("How much would you like to pay per donut (suggested price is $" + suggested_price + " each)?"))

# calculate total and respond
print("Ok, let me prepare that for you....")
total = num_donuts * cost_per * (1 + tax_rate)
print("After tax, your total is: $" + str(total))
print("Thank you for snacking! Loop back around here soon!")
