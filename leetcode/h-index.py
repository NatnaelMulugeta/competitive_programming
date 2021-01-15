def hIndex(citations):
    citations = sorted(citations)
    h, left, right = 0, 0, len(citations) - 1
    while left <= right:
        mid = left + (right-left)//2
        if citations[mid] < len(citations) - mid:
            left = mid + 1
        else:
            h = len(citations) - mid
            right = mid - 1
    return h

print(hIndex([3,0,6,1,5]))

