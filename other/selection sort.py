def selectionSort(lst):
    for i in range(len(lst)):
        j = i
        for k in range(i+1, len(lst)):
            if lst[j] > lst[k]:
                j = k
        lst[i], lst[j] = lst[j], lst[i]
    return lst

print(selectionSort([5,3,5,6,9,2]))