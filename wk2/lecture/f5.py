"""
Make a purchasing using python

    Ask the user two for item name and price (twice)
    Create a receipt:

    Item Name                       Item Price

    Shoes                           $99.99
    Hat                             $39.99


    Sub-Total                       $139.98
    Tax                             $18.20
    Grand Total                     $158.17
"""

print("Welcome to our Purchase Module")
print("You will be asked to enter two purchase items")
print("Ready? Let's go!")
item_name_1 = input("Enter Item 1 Name: ")
item_price_1 = input(f"Enter price for {item_name_1}: ")
item_price_1 = float(item_price_1)

item_name_2 = input("Enter Item 2 Name: ")
item_price_2 = float(input(f"Enter price for {item_name_2}: "))

sub_total = item_price_1 + item_price_2
tax = round(sub_total * 0.13, 2)
grand_total = round(sub_total + tax, 2)
number_of_tabs = 10
print("Item Name", '\t' * number_of_tabs, "Item Price")
print(item_name_1, "\t" * (number_of_tabs + 2), item_price_1)
print(item_name_2, "\t" * (number_of_tabs + 2), item_price_2)
print("Sub Total", '\t' * (number_of_tabs + 1), sub_total)
print("Tax", '\t' * (number_of_tabs + 2), tax)
print("Grand Total", '\t' * number_of_tabs, grand_total)
