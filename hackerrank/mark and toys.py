def maximumToys(prices, k):
    cost, count = 0, 0
    for i in sorted(prices):
        cost += i
        if cost > k:
            break
        count += 1

    return count

print(maximumToys([1,12,5,111,200,1000,10],50))
