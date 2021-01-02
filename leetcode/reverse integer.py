
def reverse(num):
    result = 0
    isNeg = False
    if num < 0:
        num = abs(num)
        isNeg = True
    while num > 0:
        new = num % 10
        result = result * 10 + new
        num = num // 10

    if result >= 2**31 - 1 or result <= -2**31:
        return 0
    elif isNeg:
        return -1 * result
    else:
        return result

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
