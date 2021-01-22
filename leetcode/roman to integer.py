def roman(s):
    result = 0

    all_romans = {"M":1000, "CM":900, "D":500, "CD": 400,
                  "C":100,"XC":90, "L":50, "XL":40,
                  "X":10, "IX":9, "V":5, "IV":4, "I":1}

    two_letters = ["CM","CD","XC","XL","IX","IV"]


    for i in two_letters:
        if i in s:
            result += all_romans[i]
            s = s.replace(i, "")

    for i in s:
        result += all_romans[i]
        s = s.replace(i, "")
    return result

print(roman('III'))
print(roman('IV'))
print(roman('IX'))
print(roman('LVIII'))
print(roman('MCMXCIV'))

