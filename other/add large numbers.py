def add_nums(n1, n2):

    isNeg1 = False
    isNeg2 = False
    
    if n1 < 0:
        n1 = abs(n1)
        isNeg1 = True
    if n2 < 0:
        n2 = abs(n2)
        isNeg2 = True

    num1 = str(n1)
    num2 = str(n2)

    if len(num1) < len(num2):
        return add_nums(num2, num1)

    lst1, lst2 = [], []
    for i in range(len(num1)-1, -1, -1):
        lst1.append(int(num1[i]))
    for i in range(len(num2)-1, -1, -1):
        lst2.append(int(num2[i]))
        
    for i in range(0, len(lst1) - len(lst2)):
        lst2.append(0)

    carry = 0
    result = []
    for i, j in zip(lst1, lst2):
        s = i + j + carry
        carry = int(s/10)
        result.append(s%10)
    if carry != 0:
        result.append(carry)
    final = "".join(str(i) for i in reversed(result))

    if isNeg1 and isNeg2:
        final = '-' + final
        return final
    elif isNeg1:
        tmp = int(final)
        tmp = tmp - 2*n1
        final = str(tmp)
        return final
    elif isNeg2:
        tmp = int(final)
        tmp = tmp - 2*n2
        final = str(tmp)
        return final
    else:
        return final
        
