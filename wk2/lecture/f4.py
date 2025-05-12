name = "Person"
age = 20
height = 150.0 # centimetres
weight = 60  # kilos

# Hi, my name is {name}
# I am {age} years old
# I am {height}cm tall and weigh {weight}kg
print("Hi, my name is", name, "\n",
      "I am ", age, " years old", "\n",
      "I am ", height, "cm tall and weigh ",
      weight, "kg", sep='')
print("*" * 20)  # **************
print("Hi, my name is " + name,
      "I am " + str(age) + " years old",
      "I am " + str(height) + "cm tall and weigh "
      + str(weight) + "kg", sep='\n')
print("*" * 20)

print(f"Hi, my name is {name}.\nI am {age} years old\nI am {height}cm tall and weigh {weight}kg.")
