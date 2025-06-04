""""
Ask the user how many countries have they visited.

Ask them to name the countries that they have visited

Ask them to name the capital cities of these countries.

"""

number_of_countries_visited = int(input("How many countries have you visited? "))
print("You will now name all of these countries")
country_names = set()
for i in range(number_of_countries_visited):
    country_names.add(input(f"Name country {i + 1} of {number_of_countries_visited} visited: "))

countries_visited = tuple(country_names)

"""
    each index of dictionary
        key: title or a look-up value
        value: a value

"""

capital_cities = dict()

for country in countries_visited:
    cap_city = input(f"What is the capital city of {country}: ")
    capital_cities[country] = cap_city

print(capital_cities)
