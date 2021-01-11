
def division(numerator, denominator):

    isNeg = False
    if numerator < 0 and denominator < 0:
        numerator, denominator = abs(numerator), abs(denominator)
    elif numerator < 0 or denominator < 0:
        numerator, denominator = abs(numerator), abs(denominator)
        isNeg = True

    numerator, denominator = str(numerator), str(denominator)
    result = ""

    
    i = 0
    temp = int(numerator[i])
    while(temp < int(denominator)):
        temp = (temp * 10 + int(numerator[i+1]))
        i += 1
    i += 1

    while((len(numerator)) > i):
        result += str(int(temp // int(denominator)))
        temp = ((temp % int(denominator)) * 10 + int(numerator[i]))
        i += 1

    result += str(int(temp // int(denominator)))

    if (len(result) == 0):
        return "0"
    return result

print(division(1248163264128256512, 125))

