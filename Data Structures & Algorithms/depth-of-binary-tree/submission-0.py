# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findMaxDepth(root, 1)
    

    def findMaxDepth(self, root: Optional[TreeNode], depth: int) -> int:
        if root == None:
            return 0
        
        if root.right == None and root.left == None:
            return depth
        
        leftM = self.findMaxDepth(root.left, depth + 1)
        rightM = self.findMaxDepth(root.right, depth + 1)
        return max(leftM, rightM)

            
        