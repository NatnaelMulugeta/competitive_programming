from collections import Counter
def isValid(s):
    
    count = Counter(s)
    val_count = Counter(count.values())

    if len(val_count) == 1:
        return "YES"

    elif len(val_count) > 2:
        return "NO"

    elif 1 in val_count.values() and (val_count[min(val_count.keys())] == 1 or (max(val_count.keys()) - min(val_count.keys()) == 1)):
            return "YES"
    else:
        return "NO"

print(isValid("aabbccddeefghi"))
print(isValid("abcc"))