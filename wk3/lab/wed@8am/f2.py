
"""
ask the user for a letter

determine if letter is a vowel or consonant
"""

text = input("Enter a letter").strip()[0]

if text in 'aeiou':
    print(text, "is a vowel")
else:
    print(text, "is a consonant")