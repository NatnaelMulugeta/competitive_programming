class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            bnum = bin(i).replace("0b", "")
            
            if len(bnum) < k:
                zeros = "0"*(k-len(bnum))
                bnum = zeros + bnum  
            
            if bnum not in s:
                return False
            
            
        return True
    