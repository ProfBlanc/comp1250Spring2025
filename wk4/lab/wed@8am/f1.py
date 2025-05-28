"""
Picnic Game

Ask the user for an item.
Ensure that the item is NOT in the picnic list
    If yes, the user cannot attend
    If no, the user can attend the picnic
"""

picnic = []
while True:  # run this loop until we decide to BREAK out in loop body
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
    
