# ask the user 3 times for their fav numbers

# for loop      =>      iterate a collection of values

# while loop    =>      iterate while a condition is met (True)

fav_nums = list()
fav_nums = []

while len(fav_nums) < 3:
    fav_nums.append(    int( input("Enter your favourite number")  )    )

print("Your", len(fav_nums), "favourite numbers are", fav_nums)


