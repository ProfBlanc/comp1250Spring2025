import sys

try:
    # user input with conversion
    # conversion with exception of str()
    # open (resource, file)
    answer = input("Enter a number: ")
    print("user answered", answer)
    print("now attempting to convert", answer, "to int")
    num = int(answer)
    print("Now printing the int")
    print(num)
except Exception as e:
    print("Uh oh! Something went wrong")
    print(e, file=sys.stderr)