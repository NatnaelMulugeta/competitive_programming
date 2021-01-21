class Solution:
    def isValid(self, s: str) -> bool:
        d = {"]" : "[", "}" : "{", ")" : "("}
        stack = []
        for i in s:
            if i in d.keys():
                if len(stack) == 0 or stack.pop() != d[i]:
                    return False
            elif i in d.values():
                stack.append(i)

        return len(stack) == 0