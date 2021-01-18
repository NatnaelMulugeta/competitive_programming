def removeDuplicates(nums):
    if len(nums) == 1:
        return len(nums)
    new = 0
    for i in range(0, len(nums)-1):
        if nums[i] != nums[i+1]:
            new += 1
            nums[new] = nums[i+1]
    return new + 1

print(removeDuplicates([1,1,1,2,2,3,3,3,4]))