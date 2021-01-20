
def sortArray(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    sortArray(left)
    sortArray(right)

    l = r = n = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            nums[n] = left[l]
            l += 1
        else:
            nums[n] = right[r]
            r += 1
        n += 1

    while l < len(left):
        nums[n] = left[l]
        l += 1
        n += 1
    while r < len(right):
        nums[n] = right[r]
        r += 1
        n += 1

    return nums


print(sortArray([5,1,1,2,0,0]))