def quickSort(arr):
    if len(arr) < 2:
        return arr
    left, equal, right = [], [], []
    equal.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        elif arr[i] > arr[0]:
            right.append(arr[i])
        else:
            equal.append(arr[i])

    return quickSort(left) + equal + quickSort(right)

print(quickSort([4,5,3,7,2]))