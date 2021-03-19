# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        
        # recursive
        
#         if not root: return
        
#         result = []
#         self.helper(root, result)
        
#         return result
    
#     def helper(self, node: TreeNode, lst: List[int]):
#         if not node: return
        
#         self.helper(node.left, lst)
#         lst.append(node.val)
#         self.helper(node.right, lst)
        
        
        # iterative
        
        if not root: return
        
        result = []
        stack = []
        
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
            
        return result
        
    