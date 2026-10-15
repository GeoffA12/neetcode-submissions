# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])
    

    def traverse(self, root: Optional[TreeNode], arr: List[int]) -> List[int]:
        if root == None:
            return arr
        
        if root.left == None and root.right == None:
            arr.append(root.val)
            return arr
        
        if root.left != None:
            arr = self.traverse(root.left, arr)
        
        arr.append(root.val)
        
        if root.right != None:
            arr = self.traverse(root.right, arr)
        
        return arr
        