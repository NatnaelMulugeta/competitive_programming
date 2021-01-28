# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return None
        
        self.path = []
        self.makeAList(root)
        
        min_dst = float('inf')
        for i in range(len(self.path)-1):
            if self.path[i+1] - self.path[i] <= min_dst:
                min_dst = self.path[i+1] - self.path[i]
        
        return min_dst
        
    def makeAList(self, root: TreeNode) -> [int]:
        if not root:
            return None
        self.makeAList(root.left)
        self.path.append(root.val)
        self.makeAList(root.right)

