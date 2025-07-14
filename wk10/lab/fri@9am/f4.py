path = "myfile.txt"
fo = open(path, "a")
text = input("Enter text: ")
fo.write(f"{text}\n")

lines = "first\n,second\n,third\n".split(",")
fo.writelines(lines)
fo.close()
