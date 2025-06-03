"""
sets
    like a list but only stores unique values
    indexing is not possible because sets are NOT ordered
    
    Q: why would i create a set. when a list would do
        - in list, manually check existance of another
        - set operations
            - intersection, difference, union, symmetric_difference
        
        -add(), remove()/discard()
        -pop(): remove a value at random
            

"""


s1 = set("hello")
print(s1)
s2 = set("cool")

print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.symmetric_difference(s2))
print(s1.difference(s2).union(s2.difference(s1)))


s1.add("z")
s2.add("y")
s1.remove("o")

s1.discard("abc")

if "abc" in s2:
    s2.remove("abc")

s2.discard("abc")

print(s1)


for item in s1:
    print(item)

#s2.append("yes")

mystery = list("hello")
mystery.remove("h")
print(mystery)

for value in "abc":
    s1.discard(value)
    
