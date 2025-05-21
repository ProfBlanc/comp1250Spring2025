name = "John"
age = 20

print(len(name) >= 3 and age < 30)
print(len(name) > 10 or age < 100)
# and => all boolean expressions must be true
# or => any boolean expression must be true

print("o" in name)  # True
print("jo" in name) # False
print("hn" in name and not age < 10)

