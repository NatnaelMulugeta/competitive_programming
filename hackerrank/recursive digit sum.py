def superDigit(n, k):
    num = 0
    for i in n:
        num += int(i)
    num = str(num) * k
    return singleSuperDigit(num)



def singleSuperDigit(n):
    if int(n) <= 9:
        return int(n)

    return singleSuperDigit(str(sum(map(int, list(n)))))

print(superDigit('148',3)) #3
print(superDigit('9875',4)) #8
print(superDigit('123',3)) #9