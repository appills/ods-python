from node import Node

class SLinkedList:
    head = False
    tail = False
    size = 0
    
    def __init__(self):
        self.head = False
        self.tail = False
        self.size = 0
    
    # get the ith node of the list
    def get(self, i):
        node = self.head
        if i > self.size:
            node = False
        else:
            count = 0
            if i == 0:
                return node
            while node and count < i:
                node = node.next
                count = count + 1
        return node
            
    # set the ith node.val to val 
    def set(self, i, val):
        node = self.get(i)
        if node:
            node.val = val
            return True
        return False

    # add val to the ith node, return new value
    def add(self, i, val):
        node = self.get(i)
        if node:
            node.val = node.val + val
            return node.val
        return False

    # append a node with val to the end of the list - the book calls this "add"
    def append(self, val):
        node = Node(val)
        if self.size == 0:
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
            self.size = self.size + 1
        return True
    
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
        if self.size == 0:
            return False
        val = self.head.val
        self.head = self.head.next
        self.size = self.size - 1
        if self.size == 0:
            self.tail = False
        return val
    
    # for queues (FIFO) 
    # we treat self.head as the front of the line
    # self.tail is then the back of the line
    # e.g. [1] -> [2], then enqueue(3) means [1]->[2]->[3]
    # dequeue() then means pop() and thus [2]->[3]
    
    def enqueue(self, val):
        return self.append(val)
    
    def dequeue(self):
        return self.pop()
    
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
        return self.size == n
        
    def count(self):
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
