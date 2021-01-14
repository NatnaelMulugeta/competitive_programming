def largestPerimeter(A):
    A = sorted(A)
    for i in range(len(A)-1,1,-1):
        if A[i] < A[i-1] + A[i-2]:
            return A[i] + A[i-1] + A[i-2]
    return 0

print(largestPerimeter([2,1,2]))
print(largestPerimeter([1,2,1]))
print(largestPerimeter([3,2,3,4]))
print(largestPerimeter([3,6,2,3]))