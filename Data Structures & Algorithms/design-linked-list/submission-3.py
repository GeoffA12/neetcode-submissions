class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

    
    def __str__(self):
        return f'Val: {self.val}'

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            node = self.getAtIndex(index)
            return node.val

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            node = Node(val, None, None)
            self.head = node
            self.tail = node
        else:
            # New head
            node = Node(val, self.head, None)
            # Set previous head prev pointer to new head
            self.head.prev = node
            # Reassign head
            self.head = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            node = Node(val, None, None)
            self.head = node
            self.tail = node
        else:
            # New tail
            node = Node(val, None, self.tail)
            # Set next pointer of current tail to the new tail
            if self.tail != None:
                self.tail.next = node
            # Reassign tail
            self.tail = node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
    
        node = self.getAtIndex(index)
        
        # Inserted node
        newNode = Node(val, node, node.prev)

        # Preserve old previous pointer to reassign its next pointer
        oldPrev = node.prev

        # Reassign prev pointer of target node at index
        node.prev = newNode

        # Reassign old previous pointer next pointer to inserted node
        oldPrev.next = newNode

        self.size += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        print(index)
        print(self.size)
        print(self.head)
        print(self.tail)
        
        node = self.getAtIndex(index)

        prev = node.prev

        next = node.next

        if prev != None:
            prev.next = next

        if next != None:
            next.prev = prev
        
        if node == self.head:
            self.head = next
        
        if node == self.tail:
            self.tail = prev
        
        self.size -= 1
    
    def getAtIndex(self, index: int):
        node = self.head
        currentIndex = 0
        while node != None:
            if index == currentIndex:
                return node
            else:
                node = node.next
            
            currentIndex += 1
        
        return None
    
    def __str__(self):
        print(f'Size: {self.size}')
        print(f'Head: {self.head}')
        print(f'Tail: {self.tail}')
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)