import re

temp = input("Enter the temperature. You decide the unit (C or F)")


regex = r"[+-]?(\d{1,2}|[01][0-5]\d)(\.\d{1,2})?\s?[cf]"

match = re.match(pattern=regex, string=temp, flags=re.I)

print(temp, "is" if match else "is NOT", "a valid temperature")
