"""
ask the user for the month
ask the user for the temp in degrees celsius

determine the season
determine which coat they should wear



comp 1250

index
0   1   2   3   4   5   6   7   8
text
C   O   M   P       1   2   5   0



"""

month = input("Enter a month. Use the full month name: ")
temperature = float(input("Enter the temperature in degrees Celsius: "))

abbr = month.lower()[0:3]
first_letter = abbr[0]

season = "unknown"
coat = "your choice"

# winter
if first_letter in 'df' or abbr == "jan":
    season = "winter"
    coat = "heavy coat"
# summer
#elif abbr == "jun" or abbr == "jul" or abbr == "aug":
#elif (first_letter == "j" or first_letter == "a") and abbr[1] == "u"    
elif abbr[1] == "u":
    season = "summer"
    if temperature < 20:
        coat = "windbreaker"
    else:
        coat = "no coat"

print(f"Given the month is", month, "and the temperature is", temperature)
print("It is the", season, "season and you should wear", coat)
