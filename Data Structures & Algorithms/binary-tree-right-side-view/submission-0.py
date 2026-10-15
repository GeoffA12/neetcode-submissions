# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    """
    1. Append the root onto the BFS queue. 
    2. Enter while loop
    3. Get the off the queue
    4. If the node is the only node on the level (size 1), it's automatically visible on the right side
    5. If there's more than 1 node, we only care to add the node furthest to the right in the queue.
    6. IMPORTANT: When adding new nodes to the queue, ensure that the left node is added before the right child node
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        res = []

        while len(q) > 0:
            size = len(q)
            for i in range(0, size):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                # This is the node that's the furthest to the right on it's level, so append it. 
                if i == size - 1:
                    res.append(node.val)
        
        return res
            
        
                
            




        