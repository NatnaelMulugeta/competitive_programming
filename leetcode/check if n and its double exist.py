class Solution:
    def checkIfExist(self, arr: [int]) -> bool:
        double = []
        for num in arr[:]:
            for d in double:
                if num * 4 == d or num == d:
                    return True
            double.append(num * 2)
            
        return False