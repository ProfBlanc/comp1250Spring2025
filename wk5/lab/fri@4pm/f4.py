# collections aka data structures
countries_visited = set()
capital_cities_of_countries = dict()

for x in range(5):
    countries_visited.add(input("What country have you visited? "))

capital_cities_of_countries = dict.fromkeys(countries_visited)
"""
    {
        "can": None,
        "usa": None,
        "mex": None
    }
"""

for country in countries_visited:
    capital_cities_of_countries[country] = input(f"Enter the capital city of {country}: ")
    
print(capital_cities_of_countries)
