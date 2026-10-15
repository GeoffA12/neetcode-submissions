# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        1. [1, 2, 3] k = 1
        2. answer is 1
        3. [2, 3, 4, 5] k = 4
        4. answer is 5
        Create an array that collects the values of the BST using pre-order traversal -- left, root, right.
        The answer is arr[k] where k is 1-indexed instead of 0-indexed.
        """
        preorderList = self.preorderTraversal(root, k, [])

        return preorderList[k - 1]

    
    def preorderTraversal(self, root: Optional[TreeNode], k: int, l: List[int]) -> List[int]:
        if root is None:
            return l
        
        if root.left == None and root.right == None:
            l.append(root.val)
            return l
        
        if root.left != None:
            l = self.preorderTraversal(root.left, k, l)
        
        l.append(root.val)

        if root.right != None:
            l = self.preorderTraversal(root.right, k, l)
        
        return l
        

