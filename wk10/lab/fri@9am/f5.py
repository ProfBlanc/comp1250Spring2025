path = "myfile.txt"
fo = open(path, "r")
# content = fo.read()  # all content
# content =fo.read(10)  # first 10 bytes (characters)
content = fo.readlines()
print(content)
fo.close()
