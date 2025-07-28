import zipfile

for i in range(1, 4):
    with open(f"test{i}.txt", "w") as file:
        file.write("Text for file test " + str(i) + ".txt file")


with zipfile.ZipFile("together.zip", "w") as zf:
    zf.write("test1.txt")
    zf.write("test2.txt")
