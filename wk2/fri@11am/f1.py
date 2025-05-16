print(True + True)
print( min(1, -1, 10, -100)  )
print( max(1, -1, 10, -100)  )
print(min("Ben", "Benny", "Benjamin"))
# print(), input(), str(), int(), float(), bool(), min(), max(), round()

# ask the user for a distance (in km)
# ask the user for a time (in hours)
# calculate the speed in km/h & m/2
# s = d/t
distance = input("Enter the distance in kilometers: ")
distance = float(distance)
time = float(input("Enter the time in hours: "))
speed_in_kph = distance / time
speed_in_kph = round(speed_in_kph, 2)

speed_in_mps = round((distance * 1000) / (time * 60 * 60) , 2)

print(f"Your travelled {distance}km in {time} hours", end=". ")
print(f"That's a speed of {speed_in_kph}km/h, which is {speed_in_mps}m/s")


