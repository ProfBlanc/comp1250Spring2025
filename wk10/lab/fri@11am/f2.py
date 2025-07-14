import re
temp = input("Enter today's raw temperature value (without metrics): ")

regex_temp = r"[\+-]?\d{1,3}(\.\d{1,2})?"
match = re.match(pattern=regex_temp, string=temp)
print(temp, "if a valid temperature" if match else "invalid temperature")

