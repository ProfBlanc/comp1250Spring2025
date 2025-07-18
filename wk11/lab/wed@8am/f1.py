with open("test.txt", "r+") as fo:
    content = fo.read(5)
    print(content)
    fo.seek(13)
    content = fo.read(5)
    print(content)
    print(fo.tell())  # where cursor is in file

    fo.truncate(20)
