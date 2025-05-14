"""
Ask the user: what is the distance between their home and school?

Output to the user: the time it will take to travel from their home to school
at a speed of 30 km/h, 40 km/h, 50 km/h

"""

distance = input("What is the distance between you home and school?")

distance = float(distance)

time_in_hours_1 = distance / 30
time_in_hours_1 = round(time_in_hours_1, 2)
print(f"Travelling {distance} km at a speed of 30 km/h will take you {time_in_hours_1} hours ")

# questions: how to transform the time in hours to time in minutes

time_in_minutes_1 = time_in_hours_1 * 60