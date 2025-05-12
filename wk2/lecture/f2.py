"""
a multi-line comment but more specifically,
triple-quotes is how you can officially document the script.
FYI 1 single .py file is known as a source_code. A second term is: module

"""

# one-line comment

# ask the user for the day of the week.
# ask the user for temperature
# output: "On {day of week}, it is {temperature} degrees Celsius

#snake_case or under_score_notation

day_of_week = input("What day of the week is it today? ")
# concatenation aka merging aka joining
# temperature = input("What is " + day_of_week + "'s temperature")
# temperature = float(temperature)

temperature = int(input("What is " + day_of_week + "'s temperature"))

print(day_of_week + "'s temperature is",
      temperature, "degrees Celsius")

print("Half of today's temperature is", temperature / 2)
