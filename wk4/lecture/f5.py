# count up from 1 to 10

# range()  => generates a series of int values
    # range(num):  0 - num (exclusively)
    # range(n1, n2):  n1 - n2 (exclusively)
    # range(n1, n2, n3):  n1 - n2 (exclusively), skipping n3 values
    

for num in range(10):
    print(num, end="\t")
print('\n',"*" * 10)    
for num in range(1, 11):
    print(num, end="\t")
    
print('\n',"*" * 10)    
for num in range(10, 0, -1):
    print(num, end="\t")
    
