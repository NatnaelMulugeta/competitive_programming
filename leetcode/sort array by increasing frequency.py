from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        nums.sort(key = lambda num: (count[num], -num))
        return nums

        
        
obj = Solution()
print(obj.frequencySort([1,2,1,1,0,2,3]))