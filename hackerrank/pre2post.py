def prefixToPostfix(prefixes):
    operators = ['+','-','/','*']
    res = []
    for prefix in prefixes:
        p = list(prefix)
        r = []
        l = len(p)
        for i in range(l-1,-1,-1):
            if p[i] in operators:
                operand1 = r[-1]
                r.pop()
                operand2 = r[-1]
                r.pop()
                r.append(operand1 + operand2 + p[i])
            else:
                r.append(p[i])
        res.append(r)
    return res

print(prefixToPostfix(['*34','+1*23','+12']))