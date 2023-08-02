class DNode:
    prev = False
    next = False
    val = None
    def __init__(self, val = None):
        self.val = val
        self.prev = False
        self.next = False

class DLinkedList:
    head = False
    tail = False
    size = 0
    
    def __init__(self):
        self.size = 0
        self.dummy = DNode(None)
        self.dummy.prev = dummy
        self.dummy.next = dummy
        
    def get_node(self, i):
        p = False
        # if the position is less than half the size, start searching from the beginning
        if i < self.size/2;
            p = self.dummy.next # this cycles to head
            c = 0
            while c < i:
                c = c + 1
                p = p.next
        else:
            p = self.dummy
            c = 0
            while c < self.size-i:
                c = c + 1
                p = p.prev
        return p
    
    def get(self, i):
        return self.get_node(i).val
    
    def set(self, i, val):
        u = self.get_node(i)
        y = u.val
        u.val = val 
        return y
    
    # given a reference to a node, w
    # we want to insert a new node, u before w
    def add_node_before(self, w, val):
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
    def add(self, i, x):
        n = self.get_node(i)
        return self.add_before(n, x)
    
    # remove w from the list
    def remove_node(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.size = self.size - 1
    
    # remove the ith node from the list
    def remove(self, i):
        node = self.get_node(i)
        self.remove_node(node)