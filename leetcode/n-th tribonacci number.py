class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        t0, t1, t2 = 0, 1, 1
        t = 0
        for _ in range(3, n+1):
            t = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t
        
        return t