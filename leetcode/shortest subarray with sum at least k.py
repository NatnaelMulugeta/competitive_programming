import heapq
class Solution:
    def shortestSubarray(self, A: [int], K: int) -> int:
        result = float('inf')
        
        heap = []
        heapq.heappush(heap, (0, -1))
        
        total = 0
        for i, num in enumerate(A):
            total += num
            while heap and total - heap[0][0] >= K:
                result = min(result, i - heapq.heappop(heap)[1])
            heapq.heappush(heap, (total, i))
            
        if result < float('inf'):
            return result
        return -1
    
      
