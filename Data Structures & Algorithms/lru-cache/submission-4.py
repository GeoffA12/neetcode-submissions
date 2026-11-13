class Node:
    def __init__(self, key, val, next, previous):
        self.val = val
        self.key = key
        self.next = next
        self.previous = previous
    
    def __str__(self):
        return f'val:{self.val}, key: {self.key}'
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.val == other.val and self.key == other.key

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.m = {}

    def get(self, key: int) -> int:
        # Retrieve the node associated with the key. Move the node to the head of the LL, since it was recently used more than the other nodes. 
        if key in self.m:
            node = self.m[key]
            head = self.head
            # Reset the tail
            if node == self.tail:
                if head != self.tail:
                    self.tail = node.previous
                    self.tail.next = None
                
            # Reset the head
            if node != self.head:
                # Fix links from prev and next pointers where the node was
                prev = node.previous
                n = node.next
                prev.next = n
                if n != None:
                    n.previous = prev

                # Fix head links
                head.previous = node
                node.next = head
                node.previous = None
                
                self.head = node
            
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.m:
            if len(self.m) + 1 > self.capacity:
                # Remove the least used node from the LL and cache, before inserting the new one. 
                # The least used node should be at the tail. 
                node = Node(key, value, None, None)
                print(f'Inserting node into map: {node.key} {node.val}')
                tail = self.tail
                if tail != None:
                    new_tail = tail.previous
                    if new_tail != None:
                        new_tail.next = None
                    else:
                        new_tail = node
                    self.tail = new_tail
                    print(f'Deleting tail node from map: {tail}')
                    del self.m[tail.key]
                else:
                    self.tail = node

                head = self.head
                head.previous = node
                node.next = head
                node.previous = None
                self.head = node
                
                self.m[key] = node

            else:
                # Just add the new node to the linked list and map at the head. This can be done without removal of an existing node, because we're underneath capacity.

                node = Node(key, value, None, None)
                head = self.head
                # Reset the head to the new node
                if head != None:
                    head.previous = node
                    node.next = head
                    self.head = node
                else:
                    self.head = node
                
                if self.tail == None:
                    self.tail = node
                
                self.m[key] = node
            
        else:
            node = self.m[key]
            node.val = value
            head = self.head
            tail = self.tail
            # Reset the tail
            if node == tail:
                if node != head:
                    self.tail = node.previous
                    self.tail.next = None
                
            if node != head:
                # Fix the pointers of the previous node when moving the target node to the head
                prev = node.previous
                n = node.next
                prev.next = n
                if n != None:
                    n.previous = prev

                # Move the target node to the head of the LL
                head.previous = node
                node.next = head
                node.previous = None
                self.head = node

            


        
