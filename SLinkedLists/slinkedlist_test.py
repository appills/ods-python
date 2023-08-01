from node import Node
from slinkedlist import SLinkedList
import unittest

class SLinkedListTest(unittest.TestCase):
        
    # Exercise 3..2    
    def test_second_last(self):
        slinked = self.get_slinkedlist()
        # this should be the body with val = 2
        body = slinked.second_last()
        self.assertEqual(2, body.val)
    
    # Exercise 3..3        
    def test_get(self):
        slinked = self.get_slinkedlist()
        # get the head
        actual = slinked.get(0)
        self.assertEqual(1, actual.val)
        # get the middle
        actual = slinked.get(1)
        self.assertEqual(2, actual.val)
        # get the tail
        actual = slinked.get(2)
        self.assertEqual(3, actual.val)
    
    # Exercise 3..3    
    def test_set(self):
        slinked = self.get_slinkedlist()
        # set the head val to 0
        slinked.set(0, 0)
        actual = slinked.get(0).val
        self.assertEqual(0, actual)
        
        # set the body to 0
        slinked.set(1, 0)
        actual = slinked.get(1).val
        self.assertEqual(0, actual)
        
        # set the tail to 0
        slinked.set(2, 0)
        actual = slinked.get(2).val
        self.assertEqual(0, actual)
    
    # Exercise 3..3    
    def test_add(self):
        slinked = self.get_slinkedlist()
        # add 1 to head -> 2
        slinked.add(0, 1)
        actual = slinked.get(0).val
        self.assertEqual(2, actual)
        
        # add 1 to body -> 3
        slinked.add(1, 1)
        actual = slinked.get(1).val
        self.assertEqual(3, actual)
        
        # add 1 to tail -> 4
        slinked.add(2, 1)
        actual = slinked.get(2).val
        self.assertEqual(4, actual) 
    
    # Exercise 3..3
    def test_removeHead(self):
        slinked = self.get_slinkedlist()
        # remove the head
        slinked.remove(0)
        # the head should now be the body node with val = 2
        self.assertEqual(2, slinked.get(0).val)
    
    # Exercise 3..3
    def test_removeTail(self):
        slinked = self.get_slinkedlist()
        # remove the tail
        slinked.remove(2)
        # the body should now be the tail and body.next should be false
        self.assertEqual(False, slinked.get(1).next)
    
    # Exercise 3..3    
    def test_removeBody(self):
        slinked = self.get_slinkedlist()
        # remove the middle
        slinked.remove(1)
        # there should now be two elements: 
        # the head with value 1 and position 0
        # the tail with value 3 and position 1
        self.assertEqual(1, slinked.get(0).val)
        self.assertEqual(3, slinked.get(1).val)
    
    # Exercise 3..4 
    def test_reverse(self):
        slinked = self.get_slinkedlist()
        slinked.reverse()
        expected = 3
        for i in slinked.values():
            self.assertEqual(i, expected)
            expected = expected - 1
            
    # Exercise 3..5 but I'm not raising an error/exception
    def test_check_size(self):
        slinked = self.get_slinkedlist()
        self.assertEqual(True, slinked.check_size(3))
        self.assertEqual(False, slinked.check_size(4))
    
    # test LIFO/FILO stack functionality
    def test_stack(self):
        # make sure it instantiated correctly
        slinked = SLinkedList()
        self.assertEqual(0, slinked.size)
        self.assertEqual(False, slinked.head)
        self.assertEqual(False, slinked.tail)
        actual = slinked.pop()
        # make sure an empty list returns False on pop()
        self.assertEqual(False, actual)
        # make sure the size didn't decrement
        self.assertEqual(0, slinked.size)
        # now push some vals, and ensure the functionality for size = 1
        slinked.push(3)
        self.assertEqual(1, slinked.size)
        self.assertEqual(3, slinked.head.val)
        self.assertEqual(3, slinked.tail.val)
        # push another, ensure fnclty for size = 2
        slinked.push(2)
        self.assertEqual(2, slinked.size)
        self.assertEqual(2, slinked.head.val)
        self.assertEqual(3, slinked.tail.val)
        # push another, ensure fnctly for size > 2
        slinked.push(1)
        self.assertEqual(3, slinked.size)
        self.assertEqual(1, slinked.head.val)
        self.assertEqual(3, slinked.tail.val)
        
        # obligatory once you pop the fun don't stop
        actual = slinked.pop()
        self.assertEqual(1, actual)
        self.assertEqual(2, slinked.size)
        self.assertEqual(2, slinked.head.val)
        self.assertEqual(3, slinked.tail.val)
        actual = slinked.pop()
        self.assertEqual(2, actual)
        self.assertEqual(1, slinked.size)
        self.assertEqual(3, slinked.head.val)
        self.assertEqual(3, slinked.tail.val)
        actual = slinked.pop()
        self.assertEqual(3, actual)
        self.assertEqual(False, slinked.head)
        self.assertEqual(False, slinked.tail)
    
    # test FIFO/LILO queue functionality
    def test_queue(self):
        # make sure it instantiated correctly
        slinked = SLinkedList()
        self.assertEqual(0, slinked.size)
        self.assertEqual(False, slinked.head)
        self.assertEqual(False, slinked.tail)
        # enqueue means we joined the end of the line, or the tail of the list
        actual = slinked.enqueue(1)
        self.assertEqual(actual, True)
        self.assertEqual(1, slinked.size)
        self.assertEqual(1, slinked.tail.val)
        self.assertEqual(1, slinked.head.val)
        
        actual = slinked.enqueue(2)
        self.assertEqual(actual, True)
        self.assertEqual(2, slinked.size)
        self.assertEqual(2, slinked.tail.val)
        self.assertEqual(1, slinked.head.val)
        # make sure dequeue obeys w.r.t head & tail
        actual = slinked.dequeue()
        self.assertEqual(1, actual)
        self.assertEqual(1, slinked.size)
        self.assertEqual(2, slinked.head.val)
        self.assertEqual(2, slinked.tail.val)
        
        
    # vaguely a data provider
    def get_slinkedlist(self):
        tail = Node(3)
        body = Node(2)
        head = Node(1)
        slinked = SLinkedList()
        slinked.push(3)
        slinked.push(2)
        slinked.push(1)
        return slinked
    
if __name__ == '__main__':
    unittest.main()