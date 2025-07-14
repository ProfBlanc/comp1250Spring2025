import re
weight = input("Enter your weight, followed by the metric (lbs or kg)")

regex_weight = r"\d{1,3}(\.[0-9]{1,2})?\s?(lbs?|kg)"

match = re.match(pattern=regex_weight, string=weight)

if match:
    print("Valid weight")
    metric = "kg" if "kg" in weight else "lbs"
    print("You entered a weight in ", metric, " metric")
    weight_value = float(weight.split(metric)[0].strip())
    print(weight_value, "is now a float")
else:
    print("Invalid weight")
