# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        
        if not root:
            return 0
        
        if root.left:
            self.dfs(root.left, root.val)
            
        if root.right:
            self.dfs(root.right, root.val)
            
        return self.total
    
    def dfs(self, root: TreeNode, parent_val: int):
        if not root:
            return 0
        
        if root and root.left and not parent_val % 2:
            self.total += root.left.val
        self.dfs(root.left, root.val)
        
        if root and root.right and not parent_val % 2:
            self.total += root.right.val
        self.dfs(root.right, root.val)
        