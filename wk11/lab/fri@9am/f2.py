filename = "test.txt"

with open(filename, "r+") as fo:
    fo.seek(10)
    text = fo.read(5)
    print(text)
    fo.readline()
    print(fo.tell())  # which byte cursor is placed

