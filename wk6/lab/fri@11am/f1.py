"""
A train has a line
a line has many stops/station
price of trip = number of stops * price
"""

routes = {
    "Lakeshore East": "Oshawa,Scarborough,Union".split(","),
    "Lakeshore West": "Oakville,Memico,Exhibition,Union".split(","),
}
presto_card_balance = 100

def take_train(station_departing:str, station_destintation:str="Union"):
    """
    determine if stations (departing, destination ) are valid
    determine which line you're travelling on
    calculate trip price & deduct from presto_card_balance
    """
    stations_are_valid = False
    which_line = None
    trip_price = 0
    for line in routes:
        print(line, routes[line])
        if station_departing in routes[line] and station_destintation in routes[line]:
            stations_are_valid = True
            which_line = line
            break
    if stations_are_valid:
        trip_price = abs( routes[which_line].index(station_departing) - routes[which_line].index(station_destintation)     ) * 3.5
    
        global presto_card_balance
        presto_card_balance -= trip_price
    
    return stations_are_valid, which_line, trip_price

r1 = take_train("Scarborough")
r2 = take_train("Oakville", "Exhibition")
print(presto_card_balance)
print(r1)
print(r2)
print(presto_card_balance)

is_valid, line, price = r1

print(is_valid, line, price)
