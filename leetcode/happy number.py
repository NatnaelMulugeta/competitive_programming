class Solution:
    def isHappy(self, n: int) -> bool:
        def process(num):
            if num == 0: return 0
            return (num % 10) ** 2 + process(num // 10)
        
        num = n
        visited = {n}
        
        while num != 1:
            num = process(num)
            
            if num in visited: return False
            visited.add(num)
            
        return True