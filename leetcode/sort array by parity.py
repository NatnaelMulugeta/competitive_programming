
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for num in A:
            odd.append(num) if num % 2 else even.append(num)
            
        return even + odd