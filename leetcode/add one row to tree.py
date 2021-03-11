# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def dfs(root, depth, n):
            if depth == d:
                node = TreeNode(v)
                
                if n == 0:
                    node.left = root
                else:
                    node.right = root
                
                return node
            
            if not root: 
                return root
            
            root.left = dfs(root.left, depth+1, 0)
            root.right = dfs(root.right, depth+1, 1)
            
            return root
            
        return dfs(root, 1, 0)
    
        