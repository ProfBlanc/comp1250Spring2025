
"""
100
10.1

10.010.10  X

-100
-111.234
0xff

Ox123

10111011    valid in decimal or binary   
"""

text = input("Enter a numerical value in either decimal, binary, octal or hexidecimal: ")

# output which base the user entered. The value in decimal

# isdigit(), isnumerical(), value in string, count()

# if "-" in text and text.count("-") <= 1:
#     print("We found", text.count("-"), "-", "symbols in the text")

# if "." in text and text.count(".") <= 1:
#     print("We found", text.count("."), ".", "symbols in the text")

if text.replace(".", "", 1).replace("-", "", 1).isdigit():
    #print("after replacing 1", ".", "and", "-", "all other characters are digits")
    print(text, "is a valid number", float(text))
