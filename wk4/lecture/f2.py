# loops = iterate / cycle through a series of values

course = "comp1250"
for character in course:
    print(character, end="\t")

# for place_holder_variable_that_represents_single_value_in_collection in collection_of_values:

num_vowels = 0
for c in course:
    if c in "aeiou":
        print(c, "is a vowel")
        num_vowels += 1

print(course, "has", num_vowels, "vowels")


