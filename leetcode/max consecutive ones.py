class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        if not nums:
            return 0
        
        result = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
            else:
                tmp = 0
                
            result = max(result, tmp)
                
        return result
        