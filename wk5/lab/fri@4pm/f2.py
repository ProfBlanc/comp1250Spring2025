# collections aka data structures
countries_visited = set()
for x in range(5):
    countries_visited.add(input("What country have you visited? "))

for country in countries_visited:
    print("You have visited", country)
