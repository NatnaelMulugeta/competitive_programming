class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
            
        for i in range(len(nums)):
            n = target - nums[i]
            if n in nums:
                if i == d[n]:
                    continue
                else:
                    return [i, d[n]]