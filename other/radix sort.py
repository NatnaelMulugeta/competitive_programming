
def radixSort(lst):
    result = [0] * len(lst)
    for x in range(max(lst)):
        count = [0] * 10
        for i in lst:
            pos = (i//10**x) % 10
            count[pos] += 1
        for i in range(1, len(count)):
            count[i] += count[i-1]
        for i in reversed(lst):
            pos = (i//10**x) % 10
            count[pos] -= 1
            new_pos = count[pos]
            result[new_pos] = i

        lst = list(result)
    
    return result

print(radixSort([4,6,8,1,8,11,0,3,7,4,7]))
