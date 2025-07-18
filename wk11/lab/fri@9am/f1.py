filename = "test.txt"
with open(filename, "w") as fo:
    fo.write("Name,Age,Grade\n")
    fo.writelines(["John,", "25,", "100\n","Mary,", "26,", "99\n"])

