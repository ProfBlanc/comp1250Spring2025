
routes = {
    "Lakeshore East": ["Oshawa", "Scarborough", "Union"],
    "Lakeshore West": ["Burlington", "Memico", "Union"]
}
presto_card_balance = 100

def take_train(station_departing, station_destination):
    """
    Determine which line you are travelling on
    Determine if stations are valid (departing and destination)
    calculate a trip price -> deduct price from presto balance
    """
    which_line = None
    are_stations_valid = False
    trip_price = 0
    for line in routes:
        # print("Word =", line, "Definition =", routes[line])
        if station_departing in routes[line] and station_destination in routes[line]:
            are_stations_valid = True
            which_line = line
            break
    
    if are_stations_valid:
        trip_price = abs(routes[which_line].index(station_departing) - routes[which_line].index(station_destination) ) * 3.5
    
    global presto_card_balance
    
    presto_card_balance -= trip_price
        
    return which_line, are_stations_valid, trip_price

print(presto_card_balance)
print(take_train("Union","Burlington"))
print(presto_card_balance)
