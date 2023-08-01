from node import Node

class SLinkedList:
    head = False
    tail = False
    size = 0
    
    def __init__(self):
        self.head = False
        self.tail = False
        self.size = 0
    
    # get the ith   
    def get(self, i):
        node = self.head
        count = 0
        if i == 0:
            return node
        while node and count < i:
            node = node.next
            count = count + 1
        return node
            
    # set the ith node.val to val - the book is ambiguous by this & add() which is why I'm creating append()
    def set(self, i, val):
        node = self.get(i)
        if node:
            node.val = val

    # add val to the ith node  
    def add(self, i, val):
        node = self.get(i)
        node.val = node.val + val
    
    # remove the ith node
    def remove(self, i):
        if self.size == 0:
            return # we have nothing to remove
        # if i = 0, we're removing the head
        if i == 0:
            self.head = self.head.next
        else:
            # else, we're removing something between
            node = self.get(i)
            # grab the next node
            nxt = node.next
            # remove the current node by setting prev.next to nxt
            prev = self.get(i-1)
            prev.next = nxt
        self.size = self.size - 1

    # per the code in the book, we push a val and not a node
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size = self.size + 1
        
    def pop(self):
        if self.head:
            n = self.head
            self.head = self.head.next
            return n
        return self.head
        
    def append(self, node):
        if self.tail:
            # in a double linked list you'd want to update node.prev as well
            self.tail.next = node
        # we'll handle no head in the future if needed
        self.tail = node
    
    # todo this, it might be a d-list thing? I thought there was constant time alg for this?
    def deque(self):
        tmp = self.tail
        self.tail = False
        return tmp
    
    # order stuff
    def reverse(self):
        prev = False
        node = self.head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        self.head = prev
            
    def values(self):
        vals = []
        node = self.head
        while node:
            vals.append(node.val)
            node =  node.next
        return vals
            

            
    def second_last(self):
        node = self.get(0)
        count = 0
        while node.next:
            count = count + 1
            node = node.next
        return self.get(count - 1)
        
    def check_size(self, n):
        return self.size() == n
        
    def size(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count = count + 1
        return count
    
    def print(self):
        n = self.head
        while n:
            print(n.val)
            n = n.next
