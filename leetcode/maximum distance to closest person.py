import itertools
class Solution:
    def maxDistToClosest(self, seats: [int]) -> int:
        start = seats.index(1)
        
        result = max(start, seats[::-1].index(1))
        
        for i, j in itertools.groupby(seats):
            if i == 0:
                gap = len(list(j))
                result = max(result, (gap+1)/2)
                
        return int(result)