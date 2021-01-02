def sockMerchant(n, ar):
    pairs = 0
    colors = []
    for i in range(n):
        if ar[i] in colors:
            pairs += 1
            colors.remove(ar[i])
        else:
            colors.append(ar[i])
    return pairs
