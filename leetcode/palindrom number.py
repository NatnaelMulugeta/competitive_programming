def isPalindrom(x):
    s = str(x)
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            return False
    return True

print(isPalindrom(121))
print(isPalindrom(-121))
print(isPalindrom(10))
