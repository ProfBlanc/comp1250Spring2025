name = "john smith"
"""
string methods
string = data type
method = action on the value


string.method
    upper(), lower(),....plenty others
"""

print(name.upper())
print(name.lower())
print(name.title())
name = "JohN SmItH"
print(name.swapcase())
print(name.isupper())
# name = "BEN"
# name = name.upper()
print(name.upper().isupper())
print(name.center(100, "*"))
print(name.ljust(100, "*"))
print(name.rjust(100, "*"))
print(name.replace(" ", "").isalpha())

value = "123.45"
print(value.isdigit())
