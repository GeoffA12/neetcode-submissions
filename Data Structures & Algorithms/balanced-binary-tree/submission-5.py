# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left != None and root.right != None:
            rightDepth = self.depth(root.right, 0)
            leftDepth = self.depth(root.left, 0)
            print(rightDepth)
            print(leftDepth)
            ans = abs(rightDepth - leftDepth) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
        
        if root.right == None and root.left != None:
            rightDepth = 1
            leftDepth = self.depth(root, 0)
            ans = abs(rightDepth - leftDepth) <= 1 and self.isBalanced(root.left)
        
        if root.left == None and root.right != None:
            leftDepth = 1
            rightDepth = self.depth(root, 0)
            ans = abs(rightDepth - leftDepth) <= 1 and self.isBalanced(root.right)
        
        return ans
    
    def depth(self, root: Optional[TreeNode], depth: int) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        leftDepth = depth
        rightDepth = depth
        if root.left != None:
            leftDepth = self.depth(root.left, depth) + 1
        
        if root.right != None:
            rightDepth = self.depth(root.right, depth) + 1
        
        maxDepth = max(leftDepth, rightDepth)

        return maxDepth

    
    def inorderTraversal(self, root: Optional[TreeNode], rHeight: int, lHeight: int, arr: List[bool]) -> Tuple[List[bool], int, int]:
        if root == None:
            return (arr, rHeight, lHeight)
        
        if root.left == None and root.right == None:
            arr.append(True)
            return (arr, rHeight, lHeight)
        
        mlHeight = lHeight
        mrHeight = rHeight
        if root.left != None:
            tup = self.inorderTraversal(root.left, 0, 0, arr)
            arr, rHeight, mlHeight = tup
            mlHeight = mlHeight + rHeight + 1
        
        if root.right != None:
            tup = self.inorderTraversal(root.right, 0, 0, arr)
            arr, mrHeight, lHeight = tup
            mrHeight = mrHeight + lHeight + 1
        
        arr.append(abs(mrHeight - mlHeight) <= 1)
        
        return (arr, mrHeight, mlHeight)
    
    # def getHeight(self, root: Optional[TreeNode], height: int) -> int:
    #     if root == None:
    #         return 0
        
    #     if root.left == None and root.right == None:
    #         return height
    #     if root.right != None and root.left != None:
    #         mRight = self.getHeight(root.right, height + 1)
    #         mLeft = self.getHeight(root.left, height + 1)
    #         if mRight > mLeft:
    #             return mRight
    #         else:
    #             return mLeft
    #     if root.left != None:
    #         height = self.getHeight(root.left, height + 1)
    #     if root.right != None:
    #         height = self.getHeight(root.right, height + 1)
        
    #     return height
        
