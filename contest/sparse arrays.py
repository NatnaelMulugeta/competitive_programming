def matchingStrings(strings, queries):
    return [strings.count(i) for i in queries]

print(matchingStrings(['ab','ab','abc'], ['ab','abc','bc']))