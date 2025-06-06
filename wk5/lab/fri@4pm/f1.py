dob = input("What is your Date Of Birth: ")
birth_country = input("What is your birth country: ")
blood_type = input("What is your blood type: ")

unchangeable_data = (dob, birth_country, blood_type)
print(type(unchangeable_data))
print(unchangeable_data)

print(unchangeable_data[0])
print(unchangeable_data[1])
print(unchangeable_data[2])

tup1 = tuple(range(1, 4))

tup2 = unchangeable_data + tup1

print(tup2)

tup3 = tup1 * 2 + unchangeable_data * 3

print("hello " * 5)

print(tup3) # (1,2,3,1,2,3, 'a','b','c', 'a','b','c', 'a','b','c')


value1, value2, value3 = unchangeable_data  # unpacking






