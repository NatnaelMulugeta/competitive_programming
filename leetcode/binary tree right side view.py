# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        if not root:
            return []
        result = [root.val]
        stack = [root]
        while stack:
            right_most = []
            for node in stack:
                if node.left:
                    right_most.append(node.left)
                if node.right:
                    right_most.append(node.right)
                    
            stack = right_most
            if stack:
                result.append(stack[-1].val)
            
        return result
        