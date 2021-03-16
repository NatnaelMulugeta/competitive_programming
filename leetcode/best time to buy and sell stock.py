class Solution:
    def maxProfit(self, prices: [int]) -> int:
        min_p = float('inf')
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i] - min_p > profit:
                profit = prices[i] - min_p
                
        return profit