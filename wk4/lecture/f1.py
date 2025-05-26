# list = data type stores multiple values

name = "John"
age = 100
temp = 17.5 

middle_name = ["jacob", "julien"]  # list variable with two values

# list = values surrounded by [ ] 

single_list_value = ["name"]  # list var with 1 value

varying_data_type_list = ["name", 123, True, 98.76]

prof = ["Ben", 100, 150.0]

name = prof[0]

"""
index
            0           1           2
value   
            Ben         100         150.0
"""
prof.append("love python") # add 1 single value to the list
prof.append(False)
prof.append(-654)

# len()  ???  # len() can be used for any collection data type
# collection data type aka iterable
    # something that you can iterate
        # loop through


# "comp 1250"        
"""
0       1       2       3       4       5       6       7       8 

-9      -8      -7      -6      -5      -4      -3      -2      -1
c       o       m       p               1       2       5       0


"""
course_code = list("comp 1250")  # constructors str(), int(), float(), bool()
age         = int("12345")
print("Constructor ", course_code)
print(course_code[-6 : -2])
print("last value = ", prof[-1], prof[  len(prof) - 1 ]   )
print("comp 1250"[2])  # "m"
print("comp 1250"[-7])
print(len("comp 1250"))
print(len(prof))

values = [123, -456, True, "cool", "beans"]
print(values[2:4]) # ???
# slicing when you can colon between two ints when refering to a list
# getting a range of values
# return data type in slicing is a list
# starting_index : ending_index_exclusive]
print("cool" in values)  # True 
print("o" in values)  # False
print("o" in values[3])  # True
print("123" in values)  # False?
print(123 in values) # True
value_to_search = -456
if value_to_search in values:
    print("Value",value_to_search, "was found at index",values.index(-456))  #1
print(values)
values.remove(123)
print(values)

value[0] = "updated value"
del value[1]
print(values)
