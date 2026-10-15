# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val, None, None)
        
        if root.val < val:
            # Move to the right
            rNode = self.insertIntoBST(root.right, val)
            root.right = rNode
        
        if root.val > val:
            # Move to the left
            lNode = self.insertIntoBST(root.left, val)
            root.left = lNode
        
        return root