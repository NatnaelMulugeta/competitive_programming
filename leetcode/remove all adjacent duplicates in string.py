class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                S = S.replace(S[i:i+2],"")    
                return self.removeDuplicates(S)
                
        return S