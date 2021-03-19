from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        
        # BFS
        
        if not root: return
        
        result = []
        
        queue = deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            
            if len(result) > level:
                result[level].append(node.val)
            else:
                result.append([node.val])
                          
            if node.left:
                queue.append((node.left, level + 1))
                
            if node.right:
                queue.append((node.right, level + 1))
                
        return result
    
    
        # iterative
    
#         if not root: return result
        
#         result = []
        
        
#         curr = [root]
#         while curr:
#             result.append([node.val for node in curr])
            
#             next_level = []
#             for node in curr:
                
#                 if node.left:
#                     next_level.append(node.left)
                
#                 if node.right:
#                     next_level.append(node.right)
                    
#             curr = next_level
            
#         return result