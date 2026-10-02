class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class TreeMap:
    
    def __init__(self):
        self.tree = []

    def insert(self, key: int, val: int) -> None:
        for node in self.tree:
            if node.key == key:
                self.remove(key)
        self.tree.append(TreeNode(key, val))

    def get(self, key: int) -> int:
        for i in range(len(self.tree)):
            node = self.tree[i]
            if node.key == key:
                return node.val
        return -1

    def getMin(self) -> int:
        if len(self.tree) == 0:
            return -1
        smallestNode = None
        smallestKey = 999999999
        for node in self.tree:
            if node.key < smallestKey:
                smallestKey = node.key
                smallestNode = node
        
        return smallestNode.val

    def getMax(self) -> int:
        if len(self.tree) == 0:
            return -1
        largestNode = None
        largestKey = -999999999
        for node in self.tree:
            if node.key > largestKey:
                largestKey = node.key
                largestNode = node
        
        return largestNode.val


    def remove(self, key: int) -> None:
        for i, node in enumerate(self.tree):
            if node.key == key:
                self.tree.pop(i)

    def getInorderKeys(self) -> List[int]:
        sortedNodes = sorted(self.tree, key=lambda node: node.key)
        sortedKeys = []
        for node in sortedNodes:
            sortedKeys.append(node.key)
        return sortedKeys
        

