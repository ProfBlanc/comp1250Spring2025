import re

text = "I live on an island by myself."
regex = r"[a-z]*i[a-z]*\s"

hits = re.findall(pattern=regex, string=text, flags=re.I)

for hit in hits:
    print(hit)


"""
validation:
    matches
        why? Entire string, starting from begening
existence of value at least once
    search
        why? determine first occurence of regex in sring
all occurences
    findall

"""