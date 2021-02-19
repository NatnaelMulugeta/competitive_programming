class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        given = ""
        result = []
        
        for num in digits:
            given += "".join(str(num))
        
        for num in str(int(given)+1):
            result.append(int(num))
            
        return result
            