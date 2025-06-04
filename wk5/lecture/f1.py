"""
tuples
    like list but immutable. cannot change/alter original content
sets
dictionaries

"""

v1 = list("hello")
v2 = tuple("hello")

v1[2] = "no L's"

print(v1, v2, sep='\n')

t1 = ("hi", "bye", True)

first, second, third, fourth = t1  # extracting / unpacking values

print(first, second, third)

print(t1[1])
print(t1[0:2])
