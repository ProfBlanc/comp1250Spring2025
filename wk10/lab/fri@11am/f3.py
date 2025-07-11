import re

regex = r"\d{3}-\d{3}-\d{4}"

text = "My number is 416-415-2000. My friends number is 416-555-1000"

hits = re.findall(regex, text)

print(hits)