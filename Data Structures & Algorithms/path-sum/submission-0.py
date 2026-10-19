# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.pathSum(root, targetSum, 0)

    def pathSum(self, root: Optional[TreeNode], targetSum: int, currentSum: int) -> int:
        if root is None:
            return False
        
        if root.left == None and root.right == None:
            if currentSum + root.val == targetSum:
                return True
            else:
                return False
        
        foundLeft = self.pathSum(root.left, targetSum, currentSum + root.val)
        
        foundRight = self.pathSum(root.right, targetSum, currentSum + root.val)
        
        if foundLeft or foundRight:
            return True
        else:
            return False


        