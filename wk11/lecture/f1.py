import sys

print("Hello World", file=open("test1.txt", "a"))

print("Error! No good!", file=sys.stderr)