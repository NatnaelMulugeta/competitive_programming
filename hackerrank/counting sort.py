
def countingSort(lst):

    result = [0] * len(lst)
    count = [0] * (max(lst)+1)
    for i in lst:
        count[i] += 1

    x = 0
    for i in range(max(lst)+1):
        for j in range(count[i]):
            result[x] = i
            x += 1

    return result


print(countingSort([3,1,1,2,1,3,2]))
