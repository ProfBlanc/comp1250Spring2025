"""
 season-temperature-coat decider

ask the user for a month
ask the user for a season-temperature

decide whether user should wear:
    a warm coat
    a light coat
    a sweater
    a t-shirt
    a rain coat

determine which season it is based on the month
base the coat on a month and temperature combination




"""

month = input("What month is it? ")
temperature = float(input("What temperature is it in degrees celsius? "))
"""
index
0   1   2   3   4   5   6   7   8
string
C   O   M   P       1   2   5   0

"     december    "
"december"


"     dec  em  ber    "
"dec  em  ber"
"""
# if month.lower() == "december":
#[first_index:second_index_not_inclusive]
first_three_chars = month.strip().lower()[0:3]  # takes first three chars of month
first_char =  first_three_chars[0]

coat = "default"
season = "unknown"

if first_char in "df" or first_three_chars == "jan":
    season = "winter"
    coat = "warm coat"
elif first_three_chars == "mar" or first_three_chars == "apr" or first_three_chars == "may":
    season = "spring"
    if temperature < 10:
        coat = "jacket or sweater"
    else:
        coat = "light coat"

print(f"Based on the values of month = {month} and temperature = {temperature}, it is the {season} season and you should wear {coat}")
