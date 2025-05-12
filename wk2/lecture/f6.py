"""
Create a module
    Allows us to calculate the number of
    kilometers we can travel based on
    - size of gas tank
    - consumption of gas tank
"""

size_of_gas_tank_in_litres = int(input("What is the size of your gas tank in litres?: "))

gas_consumption = float(input("How many litres does your gas tank consume per kilometre"))

print(f"Gas tank size is {size_of_gas_tank_in_litres}", f"Gas comsumption is {gas_consumption}", sep="\n", end=".\n")


# how to calculate number of km CAN travel on a full tank of gas
num_of_km_person_can_travel = round(size_of_gas_tank_in_litres / gas_consumption)

# Bonus: ask user what percentage/level of fuel that is currently in their car

# Bonus: ask user if they are going to make a round trip or one-way trip

# ask user for distance of trip (assume that it will be a round-trip)

trip_distance = int(input("What is your trip distance in kilometres? "))

#compute the litres of gas that this trip will take
litres_consumed_for_trip = gas_consumption * trip_distance  # one-way

litres_consumed_for_trip *= 2  # round-trip
# litres_consumed_for_trip = litres_consumed_for_trip * 2

print("Your round trip will consume", litres_consumed_for_trip, "litres",
      end="!" * 3 + "\n")
print("Your module is finished")