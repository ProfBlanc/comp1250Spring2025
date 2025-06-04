# ask the user for their top 3 fav foods
values = list()
for i in range(3):
    fav_food = input(f"What is your # {i + 1} favourite food?")
    values.append(fav_food)

print(values)

unique_values = set(values)
print(unique_values)
immutable = tuple(values)
if len(immutable) == 3:
    first, second, third = immutable
    print(first, second, third)