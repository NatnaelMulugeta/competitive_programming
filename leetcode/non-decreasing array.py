def checkPossibility(nums):
    count = 0
    current = nums[0]
    for i in range(1, len(nums)):
        if current > nums[i]:
            count += 1
            if count == 2:
                return False
            if nums[i-2] <= nums[i] or i < 2:
                current = nums[i]
        else:
            current = nums[i]
    return True

print(checkPossibility([3,4,2,3]))