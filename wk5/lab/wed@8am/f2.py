# ask the user for their top 3 fav foods
values = set()
for i in range(3):
    fav_food = input(f"What is your # {i + 1} favourite food?")
    values.add(fav_food)

print(values)