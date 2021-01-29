# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def isBadVersion(self, version) -> bool:
        pass

    def firstBadVersion(self, n: int):
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right)//2
            if self.isBadVersion(mid) and not self.isBadVersion(mid-1):
                return mid
            elif self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
            
        return mid
