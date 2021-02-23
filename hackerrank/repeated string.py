
def repeatedString(s, n):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count += int(n / len(s))

    for i in range(n % len(s)):
        if s[i] == 'a':
            count += 1

    return count
    


print(repeatedString('a', 12345600000000))
        
