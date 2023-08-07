from math import ceil

class DNode:
    prev = False
    next = False
    val = None
    def __init__(self, val = None):
        self.val = val
        self.prev = False
        self.next = False

# goal: rework this to get all returns to be DNode
class DLinkedList:
    dummy = False
    size = 0
    
    def __init__(self):
        self.size = 0
        self.dummy = DNode(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        
    def get_node(self, i):
        p = self.dummy
        # if the position is less than half the size, start searching from the beginning
        if i < (self.size / 2):
            p = self.dummy.next # this cycles to head
            c = 0
            while c < i:
                c = c + 1
                p = p.next
        else:
            c = 0
            while c < self.size-i:
                c = c + 1
                p = p.prev
        return p
    
    def get_val(self, i):
        return self.get_node(i).val
    
    def swap_val(self, i, val):
        u = self.get_node(i)
        y = u.val
        u.val = val 
        return y
    
    # given a reference to a node, w
    # we want to insert a new node, u before w
    def insert_node_before(self, w, val):
        u = DNode(val)
        u.prev = w.prev
        u.next = w
        # make the previous node point forward to the new node
        u.prev.next = u
        # make the next node (w) point prev back to the new node
        u.next.prev = u
        self.size = self.size + 1
        return u
    
    # append a new node to the list with value x
    def insert_val_before(self, i, x):
        n = self.get_node(i)
        return self.insert_node_before(n, x)
    
    # remove w from the list
    def remove_node(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.size = self.size - 1
        return w
    
    # remove the ith node from the list
    def remove_index(self, i):
        node = self.get_node(i)
        self.remove_node(node)
        return node
        
    def is_palindrome(self):
        if self.size == 0:
            return True
        if self.size == 1:
            return True
        
        is_palindrome = True
        nh = self.get_node(0)
        nt = self.get_node(self.size - 1)
        i = 0
        num_checks = ceil(self.size / 2)
        while i < self.size:
            if nh.val != nt.val:
                is_palindrome = False
            i = i + 1
            nh = nh.next
            nt = nt.prev
        return is_palindrome
        
    def truncate(self, i):
        # essentially "dequeueing" from self and "pushing" onto second
        second = DLinkedList()
        tail = self.get_node(self.size - 1) #dequeue the tail
        second_head = second.get_node(0) #push onto this
        j = 0
        size = self.size
        while j < size-i:
            u = self.remove_node(tail)
            tail = u.prev
            second_head = second.insert_node_before(second_head, u.val)
            j = j + 1
        return second
        
    def absorb(self, dll):
        dll_head = dll.get_node(0)
        # inserting before the head, due to the cyclical nature, should "append"
        head = self.get_node(0)
        i = 0
        dll_size = dll.size
        while i < dll_size:
            u = dll.remove_node(dll_head)
            dll_head = u.prev
            head = self.insert_node_before(head, u.val).prev
            
            i = i + 1
        return dll
        