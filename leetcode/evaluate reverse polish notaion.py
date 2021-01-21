class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        for token in tokens:
            if token in op:
                num1 = stack.pop()
                num2 = stack.pop()
                result = eval("int({}{}{})".format(num2, token, num1))
                stack.append(result)
            else:
                stack.append(token)

        return stack.pop()