import re
name = input("Enter your name: ")
weight = input("Enter your weight. Specify the metric (lbs or kgs): ")
# height = input("Enter your height. Specify the metric (in or m): ")

regex_name = r"[^@\$#%\^&\*\(\)=\+\?!><,;:\\\{\}\"_\[\]|]{2,}"
regex_weight = r"\d{1,3}(\.[0-9]{0,2})?\s?(lbs?|kgs?)"

valid = re.match(pattern=regex_name, string=name)
if valid:
    print("Your name of", name, "is valid")
    if "lbs" in weight:
        weight_value = float(weight.split("lbs")[0].strip())
else:
    print("The name of", name, "is invalid!")


valid = re.match(pattern=regex_weight, string=weight, flags=re.I)
if valid:
    print(weight, "is a valid weight")
else:
    print(weight, "is NOT a valid weight!")