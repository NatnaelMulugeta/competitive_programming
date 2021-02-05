import heapq
class Solution:
    def furthestBuilding(self, heights: [int], bricks: int, ladders: int) -> int:
        heap = []
        curr = 0
        while curr < len(heights)-1:
            d = heights[curr+1] - heights[curr]
            if d > 0:
                if len(heap) < ladders:
                    heapq.heappush(heap, d)
                elif ladders > 0:
                    old = heap[0]
                    if d > old:
                        heapq.heapreplace(heap, d)
                        bricks -= old
                    else:
                        bricks -= d
                else:
                    bricks -= d
                    
                if bricks < 0:
                    break
            curr += 1
                    
        return curr


