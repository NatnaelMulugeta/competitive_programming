from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        heap = []
        count = Counter(words)
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        
        result = []
        for _ in range(k):
            tmp = heapq.heappop(heap)
            result.append(tmp[1])
            
        return result