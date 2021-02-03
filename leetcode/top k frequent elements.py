from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        heap = []
        count = Counter(nums)
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
        
        return [num for freq, num in heap]
        