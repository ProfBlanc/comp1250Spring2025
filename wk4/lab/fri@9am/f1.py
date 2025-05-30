# initial picnic storage

# full list of picnic items
picnic_items = list()
# list that will serve as a history of picnic items
items_to_recite = [] 

print("Welcome to our Picnic Guessing Game")
print("You need to guess all items in the picnic before adding a unique item yourself")

while True:
    
    if len(picnic_items) > 0:
        # force user to guess items before adding a new item
        print("There are", len(picnic_items), "already added to the picnic.")
        print("You need to guess all of them before adding a new item")
        # copy picnic items to a new list to track guessed items
        items_to_recite = picnic_items[0:len(picnic_items)]
        while len(items_to_recite) > 0:
            guess = input(f"Guess an item that is already in the picnic ({len(items_to_recite)} remaining): ")
            if guess in items_to_recite:
                print("Yes!", guess, "is in the picnic list")
                items_to_recite.remove(guess)
                continue
            print("Sorry, but", guess, "is NOT in the list")
            break
    
    if len(picnic_items) > 0 and len(items_to_recite) != 0:
        print("Unfortunately, you cannot attend or add an item to the picnic")
        break
            
    item = input("What will you bring to the picnic? ")
    if item not in picnic_items:
        picnic_items.append(item)
        print("Great! You can bring", item, "to the picnic")
    else:
        print("Sorry, but", item, "already exists in the picnic list")
        break
