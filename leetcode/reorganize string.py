from collections import defaultdict

def reorganizeString( S):
    result = []
    count = defaultdict(int)
    for c in S:
        count[c] += 1

    lst = [(-n, n, c) for c, n in count.items()]
    lst = sorted(lst)
    _, n, c = lst[0]

    i = 0
    while i < n:
        result.append([c])
        i += 1

    pos = 0
    for _, n, c in lst[1:]:
        for _ in range(n):
            result[pos].append(c)
            pos = (pos + 1) % len(result)

    if len(result) > 1 and len(result[-2]) == 1:
        return ""

    return "".join(map(lambda x: "".join(x), result))

print(reorganizeString("nnnattyyn"))
print(reorganizeString("aaab"))