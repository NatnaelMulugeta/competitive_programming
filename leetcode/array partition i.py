class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(len(nums)-2, -1, -2):
            max_sum += min(nums[i], nums[i+1])
            
        return max_sum