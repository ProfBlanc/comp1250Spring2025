passengers = {
    "compact": set(),  # max 4
    "van": set(),      # max 7
    "suv": set(),      # max 6
}
passenger_keys = list(passengers)
max_passengers = dict.fromkeys(passenger_keys)

max_passengers[passenger_keys[0]] = 4
max_passengers[passenger_keys[1]] = 7
max_passengers[passenger_keys[2]] = 6

def ride(passenger_name, car_type, pickup, destination):
    global passengers
    if isinstance(car_type, str) and car_type in passengers:
        print(car_type, "IS available")
        
        chosen_vehicle = passengers[car_type]
        
        if len(chosen_vehicle) == max_passengers[car_type]:
            print("The", car_type, "is full")
        else:
            print(car_type, "has", max_passengers[car_type] - len(chosen_vehicle), "spot available")
            chosen_vehicle.add(passenger_name)
            
        
        
    else:
        print(car_type, "NOT available")
        
        
ride("me", "compact", "my house", "school")
print(passengers)
ride("you", "compact", "your house", "school")    
print(passengers)
ride("friend", "compact", "place 1", "school")    
ride("parent", "compact", "place 2", "school") 
ride("other", "compact", "place 3", "school")    
print(passengers)

