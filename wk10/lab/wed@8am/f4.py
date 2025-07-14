import os

path = os.path.join("test1", "test2", "text.txt")
#path = r"test1\test2\text.txt"

fo = open(path, "w")
#fo.write("This is cool, i like this\n")

lines = "Hello world\n,This is cool, i like this\n".split(",")
print(type(lines))
fo.writelines(lines)
fo.close()