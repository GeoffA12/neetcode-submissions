class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root == None:
            self.root = TreeNode(key, val)
        else:
            node = self.root
            self.insert_node(node, key, val)
    
    def insert_node(self, node, key: int, val: int) -> None:
        if node == None:
            r = TreeNode(key, val)
            return r
        if node.key < key:
            r = self.insert_node(node.right, key, val)
            node.right = r
            return node
        elif node.key > key:
            l = self.insert_node(node.left, key, val)
            node.left = l
            return node
        else:
            node.val = val
            return node

    def get(self, key: int) -> int:
        return self.get_node(self.root, key).val
    
    def get_node(self, node, key) -> TreeNode:
        if node == None:
            return TreeNode(-1, -1)
        if node.key < key:
            rv = self.get_node(node.right, key)
            return rv
        elif node.key > key:
            rv = self.get_node(node.left, key)
            return rv
        else:
            return node

    def getMin(self) -> int:
        min_node = self.get_min_node(self.root)
        if min_node is None:
            return -1
        else:
            return min_node.val
    
    def get_min_node(self, node) -> TreeNode:
        if node is None:
            return None
        while node.left != None:
            node = node.left
        return node

    def getMax(self) -> int:
        max_node = self.get_max_node(self.root)
        if max_node is None:
            return -1
        else:
            return max_node.val
    
    def get_max_node(self, node) -> TreeNode:
        if node is None:
            return None
        while (node.right):
            node = node.right
        return node

    def remove(self, key: int) -> None:
        if self.root == None:
            return None
        else:
            self.root = self.remove_node(self.root, key)

    def remove_node(self, node, key) -> TreeNode:
        if node == None:
            return None
        if node.key < key:
            r = self.remove_node(node.right, key)
            node.right = r
            return node
        elif node.key > key:
            l = self.remove_node(node.left, key)
            node.left = l
            return node
        else:
            # We've found the key/node to delete. 
            if node.left == None and node.right == None:
                return node.left
            elif node.left == None and node.right != None:
                # Return the successor, which is the right node. 
                return node.right
            elif node.right == None and node.left != None:
                # Return the successor, which is the left node
                return node.left
            else:
                r = node.right
                while r.left != None:
                    r = r.left
                node.val = r.val
                node.key = r.key
                c = self.remove_node(node.right, r.key)
                node.right = c
                return node
        

    def getInorderKeys(self) -> List[int]:
        return self.inorder_keys(self.root, [])
    
    def inorder_keys(self, node, keys) -> List[int]:
        if node == None:
            return keys
        
        updated_keys = keys
        if node.left != None:
            updated_keys = self.inorder_keys(node.left, keys)
        
        if node.right == None:
            updated_keys.append(node.key)
            return updated_keys
        else:
            updated_keys.append(node.key)
            updated_keys = self.inorder_keys(node.right, updated_keys)
            return updated_keys
        

