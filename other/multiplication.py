def multiplication(one, two):

    isNeg = False
    if one < 0 and two < 0:
        one, two = abs(one), abs(two)
    elif one < 0 or two < 0:
        one, two = abs(one), abs(two)
        isNeg = True

    num1, num2 = str(one), str(two)
    len1, len2 = len(num1), len(num2)
    index1, index2 = 0, 0
    product = [0] * (len1 + len2)

    i = len1 - 1
    while i >= 0:
        carry = 0
        n1 = int(num1[i])
        index2 = 0
        j = len2 - 1
        while j >= 0:
            n2 = int(num2[j])
            s = n1 * n2 + product[index1+index2] + carry
            product[index1+index2] = s % 10
            carry = s // 10
            index2 += 1
            j-=1

        if carry > 0:
            product[index1+index2] += carry
        index1 += 1
        i-=1

    length = len(product) - 1
    while length>=0 and product[length]==0:
        length -= 1
    if length == -1:
        return "0"
    result = ""
    while length >= 0:
        result += str(product[length])
        length -= 1

    if isNeg:
        return "-" + result
    return result

print(multiplication(1564895312646589962487, 698563247815469864))
print(multiplication(-1564895312646589962487, 698563247815469864))
print(multiplication(1564895312646589962487, -698563247815469864))
print(multiplication(-1564895312646589962487, -698563247815469864))
