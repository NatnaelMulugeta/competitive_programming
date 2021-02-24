from collections import Counter

class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        result = []
        count = Counter(nums)
        
        for num in count:
            if count[num] == 1: result.append(num)
                
        return result