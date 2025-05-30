# continually ask the user to input 5 unique integer values to a list

values = []
target_num_of_values = 3
print(f"We will force you to enter {target_num_of_values} unique values. Enter nothing to end this script")
while len(values) < target_num_of_values:
    entry = input("Enter a non-negative integer value")
    if entry.strip().isdigit():
        print(entry, "is an non-negative integer")
        values.append(int(entry.strip()))
        print("There are", len(values), "values in our list")
        if target_num_of_values - len(values) > 0:
            print("You need to input", target_num_of_values - len(values), "more values")
    else:
        print("Sorry, but", entry, "is not a non-negative number")
        if len(entry.strip()) == 0:
            print("you inputted a blank entry. We will exit the program")
            break
