
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


def height(root):
    if root == None:
        return -1
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)

