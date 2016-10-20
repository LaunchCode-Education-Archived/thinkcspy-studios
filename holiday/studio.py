"""
Studio: Holiday
"""

# get input: departure day (0-6) and duration
departure_day = input("Which day are you leaving on? (0=Sun, 1=Mon, etc)")
departure_day = int(departure_day)

duration = input("How many days will you be done?")
duration = int(duration)

# calculate return day and respond
return_day = (departure_day + duration) % 7
print("You will return on day", return_day)
