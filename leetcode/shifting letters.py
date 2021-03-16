class Solution:
    def shiftingLetters(self, S: str, shifts: [int]) -> str:
        start = ord('a')
        shift = sum(shifts) % 26
        result = []
        
        for i, c in enumerate(S):
            val = ord(c) - start
            temp = (val + shift) % 26
            
            curr = chr(start + temp)
            result.append(curr)
            
            shift = (shift - shifts[i]) % 26
            
        return "".join(result)
            