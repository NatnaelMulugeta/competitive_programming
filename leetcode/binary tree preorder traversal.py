# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> [int]:
        
        # recursive
        
#         if not root: return
        
#         result = []
#         self.helper(root, result)
        
#         return result
    
#     def helper(self, node: TreeNode, lst: List[int]):
#         if not node: return
        
#         lst.append(node.val)
#         self.helper(node.left, lst)
#         self.helper(node.right, lst)

        
        # iterative
        
        if not root: return
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result
        