# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        1. Go through each subtree. 
        2. Swap self.left and self.right
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        new_root_right = root.left
        root.left = root.right
        root.right = new_root_right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
