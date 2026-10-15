# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        1. Find the child nodes. Keep track of ancestors when searching. 
        2. If the child isn't found at current node.left, move to the left. You know that the ancestor isn't 
        if root.val == q or if root.val == p:
            return root
        # Gate for early exit on ancestor - means we branched p is in the left subtree, q is in the right. By definition of BST, this must be the ancestor
        if root.val > q (or p)
        and if root.val < q (or p) ancestor is root:
            return root

        if root.val < p and q
        traverse left, 

        if root.val > p and q
        traverse right, run split check
        p = 3, q = 8
        1. Root [5] -> [3]
        2. Check for equality on root.val against p or q ? -> false
        3. Return 5

        p = 3 and q = 4
        1. Root [5] -> traverse left
        2. Root []
        """
        if root == None:
            return root
        # We branched. So the answer is root. 
        if (root.val > q.val and root.val < p.val) or (root.val < q.val and root.val > p.val):
            return root
        
        # Because of how we traverse, we know p and q are in the same subtree
        if root.val == q.val or root.val == p.val:
            return root
        
        if root.val < p.val and root.val < q.val:
            answer = self.lowestCommonAncestor(root.right, p, q)
        
        if root.val > p.val and root.val > q.val:
            answer = self.lowestCommonAncestor(root.left, p, q)

        return answer

