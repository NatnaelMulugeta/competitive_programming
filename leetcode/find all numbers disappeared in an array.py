class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        result = []
        
        for num in nums:
            if num < 0:
                num = abs(num)
            
            nums[num-1] = -1 * abs(nums[num-1])
            
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
                
        return result

