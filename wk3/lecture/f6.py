"""
ask the user for their first name
determine if their first name only contains alphabetical letters
    error message if not
"""
name = input("Enter your first name")
name = name.strip()  #  '   Ben   ' => 'Ben'
                     # ' Ben Blanc  ' => 'Ben Blanc'

if name.isalpha() and len(name) >= 3 \
        and ('a' in name.lower()
             or 'e' in name.lower()
             or 'i' in name.lower()
             or 'u' in name.lower()
             or 'y' in name.lower()
             or 'o' in name.lower()):

    print("you entered a valid name")
else:
    print(name, "is invalid")