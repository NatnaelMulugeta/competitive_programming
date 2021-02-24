class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        numbers = {}
        
        for i, num in enumerate(nums):
            if num in numbers.keys():
                numbers[num].append(i)
            else:
                numbers[num] = [i]
        
        for val in numbers.values():
            if len(val) > 1:
                for i in range(len(val)-1):
                    if val[i+1] - val[i] <= k:
                        return True         
                        
        return False