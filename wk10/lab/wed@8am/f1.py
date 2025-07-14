import re

text = "I love python and java and javascript and all programming languages"
#regex = r"\s[a-z]{4,}\s"
regex = r"i"

#matches = re.search(pattern=regex, string=text)

matches = re.match(pattern=regex, string=text, flags=re.I)

if matches:
    print("This regex was found")
    print(matches.group(0))
    print("Starting index = ", matches.start())
    print("Ending index = ", matches.end())
else:
    print("regex was NOT found")
