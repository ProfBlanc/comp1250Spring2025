word = "education".upper()

print("Guess a mysterious word")

blanks = "___"
space = " "

to_display = f"{blanks}{space}" * len(word)

print(to_display)

print("You have three chances to guess")

letter = input("Chance 1: Enter a letter")
first_letter = letter.strip().upper()[0]


if first_letter in word:
    print("Great news!", first_letter, "is in the word")

    location_of_letter = word.index(first_letter)

    to_display = to_display.split(space)
    # series of values
    # 0: ___
    # 1: ___
    # 2: ___
    # 3: ___
    # 4: ___
    to_display[location_of_letter] = first_letter

    # series of values
    # 0: ___
    # 1: ___
    # 2: U
    # 3: ___
    # 4: ___

    to_display = space.join(to_display)

else:
    print("Sorry but", first_letter, "is NOT in the word")

print(to_display)

##################

letter = input("Chance 2: Enter a letter")
second_letter = letter.strip().upper()[0]


if second_letter in word:
    print("Great news!", second_letter, "is in the word")

    location_of_letter = word.index(second_letter)

    to_display = to_display.split(space)
    to_display[location_of_letter] = second_letter

    to_display = space.join(to_display)

else:
    print("Sorry but", second_letter, "is NOT in the word")

print(to_display)
