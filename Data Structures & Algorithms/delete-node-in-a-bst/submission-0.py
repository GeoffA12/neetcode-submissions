# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        There are 3 cases for node deletion in a BST. 
        1. 0 children - node is just a leaf so delete it and return its left/right subtree as the new root
        2. 1 child - same as above. Just check whether the left or right is None. Return that node as the new subtree
        3. 2 children. Find the target node, and the smallest node in the right subtree of the target. Swap the node values of the target and the smallest right subtree node. Then, recursively call deleteNode on the smallest right subtree node you just found.
        """

        if root == None:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right == None and root.left == None:
                return root.right
            if root.right != None and root.left == None:
                return root.right
            if root.left != None and root.right == None:
                return root.left
            replacement = self.getMinNode(root.right)
            root.val = replacement.val
            root.right = self.deleteNode(root.right, replacement.val)
        
        return root

    
    def getMinNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        while root.left != None:
            root = root.left
        
        return root
        