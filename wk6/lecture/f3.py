
result_history = list()  # global scope

def calculate(n1:float, op:str, n2:float)->float:
    global result_history
    if (isinstance(n1, int) or isinstance(n1,float)) and (isinstance(n2, int) or isinstance(n2,float)) and isinstance(op, str) and len(op) <= 2:
        
        if op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "**":
            result = n1 ** n2
        elif op == "/" and n2 != 0:
            result = n1 / n2
        elif op == "%":
            result = n1 % n2
        elif op == "+":
            result = n1 + n2
        else:
            result = 0.0
        result_history.append(result)
        return result
    else:
        return 0.0  

#print(n1)
res = calculate(10, "**", 2)
print(res)
res = calculate(10, "*", 2)
print(res)
print(result_history)
