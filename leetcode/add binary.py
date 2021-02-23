class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        
        a_lst, b_lst = [c for c in a], [c for c in b]
        while a_lst or b_lst:
            if not a_lst: a_lst = ['0']
            if not b_lst: b_lst = ['0']
                
            curr_sum = int(a_lst.pop()) + int(b_lst.pop()) + carry
            if curr_sum < 2:
                result += str(curr_sum)
                carry = 0
            elif curr_sum == 2:
                result += "0"
                carry = 1
            else:
                result += "1"
                carry = 1
                
        if carry: result += "1"
        return result[::-1]