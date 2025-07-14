import re

text = ("Hello, my phone number is 416-415-2000. "
        "My address is 160 kendal Avenue")

pattern = r"\d{3}-\d{3}-\d{4}"

#match = re.match(pattern=pattern, string=text)
match = re.search(pattern=pattern, string=text)

print(match)
print(match.group(0))
print(match.start())
print(match.end())
