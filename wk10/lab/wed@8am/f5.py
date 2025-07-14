import os

path = os.path.join("test1", "test2", "text.txt")

fo = open(path, "r")

#content = fo.read(15)
# content = fo.readline()
content = fo.readlines()
print(repr(content))
fo.close()
