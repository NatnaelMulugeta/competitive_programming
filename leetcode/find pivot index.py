class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        left = 0
        right = sum(nums[1:])
        for i in range(len(nums)-1):
            if left == right:
                return i
            else:
                left += nums[i]
                right -= nums[i+1]
                
        if left == right: return i+1
        return -1
        
