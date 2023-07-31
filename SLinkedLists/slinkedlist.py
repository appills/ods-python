from node import Node

class SLinkedList:
    head = False
    
    def __init__(self, head):
        self.head = head

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
    
    # get the ith   
    def get(self, i):
        node = self.head
        count = 0
        if i == 0:
            return node
        while count < i:
            node = node.next
            count = count + 1
        return node
            
    # set the ith node to val
    def set(self, i, val):
        node = self.get(i)
        node.val = val
        
    # add val to the ith node  
    def add(self, i, val):
        node = self.get(i)
        node.val = node.val + val
    
    # remove the ith node
    def remove(self, i):
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
            
    def second_last(self):
        node = self.get(0)
        count = 0
        while node.next:
            count = count + 1
            node = node.next
        return self.get(count - 1)
        
    def check_size(self, n):
        return self.size() == n
    
    # lol could've just counted self.values()
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
