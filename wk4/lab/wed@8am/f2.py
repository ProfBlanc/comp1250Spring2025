"""
Picnic Game & Memory Game


"""

picnic = ["water"]
while True:  # run this loop until we decide to BREAK out in loop body
    
    items_to_guess = picnic[0:len(picnic)]  # copy the values of a list 
    
    while len(items_to_guess) > 0:
        previous_item = input("Enter a previous item")
        if previous_item in items_to_guess:
            items_to_guess.remove(previous_item)
            print("Yes", previous_item, "is found in picnic list")
            continue # skip rest of loop body, go to start of loop
        print("Sorry but", previous_item, "is not in the list")
        break
    
    if len(items_to_guess) != 0:
        print("You did not correctly guess all previous items")
        print("The game is over")
        break
    
    item = input("What item will you bring to the picnic? ")
    if item in picnic:
        print("Sorry, but", item, "is not unique")
        print("You are not allowed to attend the picnic")
        break
    print("Nice! You can bring", item, "to the picnic")
    picnic.append(item)
    print("Enter another item")

print("There are", len(picnic), "items in the picnic list")
print("Here are the items:", ", ".join(picnic))
    
