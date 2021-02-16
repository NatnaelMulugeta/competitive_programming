# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        
        curr = [root]
        reverse = False
        while curr:
            if reverse: result.append([node.val for node in curr[::-1]])
            else: result.append([node.val for node in curr])
                
            next_level = []
            for node in curr:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
                    
            curr = next_level
            reverse = not reverse
            
        return result
        
        
        