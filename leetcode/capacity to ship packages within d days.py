class Solution:
    def shipWithinDays(self, weights: [int], D: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.helper(weights, mid) > D:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return hi + 1

        
    def helper(self, weights, mid):
        days = 1
        curr = mid
        for weight in weights:
            if weight > curr:
                curr = mid
                days += 1
            curr -= weight
            
        return days
        
              