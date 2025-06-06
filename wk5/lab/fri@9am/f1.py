"""
Continually ask user how many country they have visited
    once user input a blank response, exit the loop

For each country they user inputted, ask the user to inpput the cpital city

Ouptut the list (humanly speaking) of countries and their capital cities
"""

# variables 
user_input = "nothing"
countries = set()
capital_city_of_country = dict()

while len(user_input) > 0:
    user_input = input("Enter a country that you have visit: ").strip().lower().title()
    if len(user_input) > 0:
        countries.add(user_input)

print("You have been to", len(countries), "countries. Good for you!")
print("You will not enter the capital city for each of the ", len(countries), "countries")

# transform a list, tuple, set into a diction
capital_city_of_country = dict.fromkeys(countries)
print(capital_city_of_country)

for country in countries:
    user_input = input(f"What is the capital city of {country}? ").lower().title()
    capital_city_of_country[country] = user_input

print("Here is the result")

for each_key in capital_city_of_country:
    print(f"The capital city of {each_key} is {capital_city_of_country[each_key]}")
    
