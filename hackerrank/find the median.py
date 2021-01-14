def findMedian(arr):
    mid = len(arr)//2
    return sorted(arr)[mid]

print(findMedian([0,1,2,4,6,5,3]))