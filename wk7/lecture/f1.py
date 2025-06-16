import calculator
# import wk1.lecture.f1

# help(calculator)
print(calculator.allowed_operations)
calculator.allowed_operations = "foo"
print(calculator.allowed_operations)
print(calculator.add(11111.1, 222222.2))
#print(calculator.add("a", "b"))
print(calculator.calculate(11111, '-', 2))
print(calculator.calculate("4", '-', "2"))
