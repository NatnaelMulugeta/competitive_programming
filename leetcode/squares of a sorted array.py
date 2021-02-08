import bisect
import heapq
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        
        heapq.heapify(nums)
        
        while nums:
            result.append(heapq.heappop(nums))
            
        return result
        
#         result = []
        
#         for num in nums:
#             bisect.insort_right(result, num**2)
            
#         return result
        