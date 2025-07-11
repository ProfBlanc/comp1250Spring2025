import re

text = ("Hello, my phone number is 416-415-2000. "
        "My address is 160 kendal Avenue. 415-555-5000")

pattern = r"\d{3}-\d{3}-\d{4}"

#match = re.match(pattern=pattern, string=text)
match = re.findall(pattern=pattern, string=text)

print(repr(match))
