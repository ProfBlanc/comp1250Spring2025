# ask the user to input a word
# a word is
    # at least 1 character
        # a I
    # at least 1 vowel
    # by, my, why  # y is considered the vowel

# whether word is valid or not

word = input("Enter a word: ")

if len(word) > 0:
    vowels = list("aeiou")  # word = "hello"
    has_vowel = False
    for vowel in vowels:
        if vowel in word.lower():
            has_vowel = True
            break
    if (not has_vowel and "y" in word) or has_vowel:
        print(word, "is valid")
    else:
        print(word, "in NOT valid")
    
else:
    print("A word must be at least 1 character")
