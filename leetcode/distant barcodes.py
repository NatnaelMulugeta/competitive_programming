from collections import defaultdict

def rearrangeBarcodes(barcodes):
    result = []
    count = defaultdict(int)
    for c in barcodes:
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

    final = []
    for i in result:
        for j in i:
            final.append(j)
    return final

print(rearrangeBarcodes([1,1,1,2,2,2]))