"""
Picnic Memory Game
"""
picnic_items = list()
items_to_recite = []

game_over = False

print("Explain game to user")
while not game_over:
    # determine if user needs to recite items before adding new items
    if len(picnic_items) > 0:
        # pass # need to recite items 
        items_to_recite = picnic_items[0:len(picnic_items)]
        print("You need to guess", len(items_to_recite), "before you can add a new item")
        while len(items_to_recite) > 0:
            guess = input(f"Guess 1 of {len(items_to_recite)}: ")
            if guess in items_to_recite:
                items_to_recite.remove(guess)
                print("YES", guess, "is in the list")
                continue
            game_over = True
            print("Sorry but", guess, "is not in the picnic list")
            break
    if game_over:
        break
    # add new items to the picnic
    item = input("Enter an item: ")
    """
    if item not in picnic_items:
        picnic_items.append(item)
        print(item, "was added to picnic list")
        continue
    print(item, "is already in the picnic list")
    game_over = True
    """
    """
    if item in picnic_items:
        print(item, "is already in the picnic list")
        game_over = True
        continue
    picnic_items.append(item)
    print(item, "was added to picnic list")
    """
    if item in picnic_items:
        print(item, "is already in the picnic list")
        game_over = True
    else:
        picnic_items.append(item)
        print(item, "was added to picnic list")

    
    
print("There were", len(picnic_items), "items added to the picnic")
print("Items were", ", ".join(picnic_items))
