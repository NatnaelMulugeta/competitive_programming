def insertionSort(lst):
    i = 1
    while i < len(lst):
        j = lst[i]
        k = i - 1
        while k >= 0 and j < lst[k]:
            lst[k+1] = lst[k]
            k -= 1
        lst[k+1] = j
        i += 1
    return lst

print(insertionSort([5,3,5,6,9,2]))