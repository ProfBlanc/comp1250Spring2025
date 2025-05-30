picnic_list = list()
items_to_recite = []

while True:
    
    # user needs to recite values already in the picnic_list
    if len(picnic_list) > 0:
        # user has to recite
        # copy the picnic_list contents
        # why? b/c, I need to remove correctly guessed items
        items_to_recite = picnic_list[0:len(picnic_list)]
        while len(items_to_recite) > 0:
            print("You have to guess", len(items_to_recite), "items of the picnic list")
            guess = input("Enter a guess: ")
            
            if guess in items_to_recite:
                print("Yes!", guess, "is in the picnic list")
                items_to_recite.remove(guess)
            else:
                print("Sorry, but", guess, "is not in the picnic")
                break
            
    if len(picnic_list) > 0 and len(items_to_recite) > 0:
        print("You lost!")
        break
    
    # user needs to add a unique value in the picnic_list
    item = input("What is the new item that you will add to the picnic list? ")
    if item not in picnic_list:
        picnic_list.append(item)
        print(item, "was added to the picnic")
    else:
        print("Sorry, but", item, "is already in the list")
        break
    
