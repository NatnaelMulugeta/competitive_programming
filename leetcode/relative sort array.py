def relativeSortArray(arr1, arr2):
    result, lst = [], []

    for i in arr1:
        if i not in arr2:
            lst.append(i)

    for i in arr2:
        for j in arr1:
            if i == j:
                result.append(j)

    result += sorted(lst)

    return result

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))