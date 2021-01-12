def bubbleSort(lst):
    for i in range(len(lst)-1):
        k = i+1
        for j in range(len(lst)-k):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubbleSort([5,3,5,6,9,2]))
