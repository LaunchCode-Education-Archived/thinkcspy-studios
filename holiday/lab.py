"""
Lab: Holiday
"""

departure_day = input("What day are you leaving? ")
departure_day = int(departure_day)

trip_length = input("How long will you be gone (in days)? ")
trip_length = int(trip_length)

return_day = (departure_day + trip_length) % 7
print("You will return on day:", return_day)
