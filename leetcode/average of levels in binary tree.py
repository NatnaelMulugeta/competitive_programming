# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:
        result = []
        
        peer_nodes = [root]
        while peer_nodes:
            level_sum = 0
            new_level = []
            for node in peer_nodes:
                level_sum += node.val
                
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
                    
            result.append(level_sum / len(peer_nodes))
            peer_nodes = new_level
            
        return result
        
        