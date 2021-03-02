class Solution:
    def distributeCandies(self, candyType: [int]) -> int:
        # typeCount = Counter(candyType)
        typeCount = set(candyType)
        
        if len(typeCount) < len(candyType)//2:
            return len(typeCount)
        
        elif len(typeCount) >= len(candyType)//2:
            return len(candyType) // 2