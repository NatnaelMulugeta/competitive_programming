def pancakeSort(lst):
    result = []

    for i in range(len(lst), 0, -1):
        idx = lst.index(i)

        lst[:idx+1] = lst[:idx+1][::-1]
        lst[:i] = lst[:i][::-1]

        result.append(idx + 1)
        result.append(i)

    return result

print(pancakeSort([3,2,4,1]))
