
def twoSum(nums, target):
    l = len(nums)
    d = {}
    for i in range(l):
        d[nums[i]] = i
    for i in range(l):
        a = target - nums[i]
        if a in nums:
            if i == d[a]:
                continue
            else:
                return [i, d[a]]
        

