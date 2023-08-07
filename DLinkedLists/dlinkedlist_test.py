from dlinkedlist import DNode, DLinkedList
import unittest

class DLinkedListTest(unittest.TestCase):
    
    def test_can_create_instance(self):
        dlinked = DLinkedList()
    
    # Exercise 3..7    
    def test_is_palindrome(self):
        dlinkeds = self.dlinkedlist_palindrome_provider()
        i = 0
        for dl in dlinkeds:
            if i == 0:
                self.assertEqual(True, dl.is_palindrome())
            elif i % 2 == 0:
                self.assertEqual(False, dl.is_palindrome())
            else:
                self.assertEqual(True, dl.is_palindrome())
            i = i + 1

    # Exercise 3..8
    def test_rotate(self):
        dlinked = self.get_dlinkedlist()
    # Exercise 3..9
    def test_truncate(self):
        dlinked = self.get_dlinkedlist(5)
        self.assertEqual(5, dlinked.size)
        # truncate at position 2
        second = dlinked.truncate(2)
        #dlinked.size should be i = 2
        self.assertEqual(2, dlinked.size)
        self.assertEqual(3, second.size)
        #dlinked vals should be 1, 2
        self.assertEqual(1, dlinked.get_val(0))
        self.assertEqual(2, dlinked.get_val(1))
        #second vals should be 3,4,5
        self.assertEqual(3, second.get_val(0))
        self.assertEqual(4, second.get_val(1))
        self.assertEqual(5, second.get_val(2))
        
    # Exercise 3..10
    def test_absorb(self):
        dlinked = self.get_dlinkedlist()
    # Exercise 3..11
    def test_deal(self):
        dlinked = self.get_dlinkedlist()
    # Exercise 3..12
    def test_reverse(self):
        dlinked = self.get_dlinkedlist()
    # Exercise 3..13.1
    def test_take_first(self):
        dlinked = self.get_dlinkedlist()
    # Exercise 3..13.2
    def test_merge(self):
        dlinked = self.get_dlinkedlist()
    # Exercise 3..13.3
    def test_sort(self):
        dlinked = self.get_dlinkedlist()
    
    # vaguely a data provider
    def get_dlinkedlist(self, n = 3):
        dlinked = DLinkedList()
        for i in range(0, n):
            val = i + 1
            dlinked.insert_val_before(i, val)
        return dlinked
        
    def dlinkedlist_palindrome_provider(self):
        ls = []
        #0, palindrome-1
        dlinked = DLinkedList()
        dlinked.insert_val_before(0, 1)
        ls.append(dlinked)
        
        #1, palindrome-2
        dlinked = DLinkedList()
        dlinked.insert_val_before(0, 1)
        dlinked.insert_val_before(1, 1)
        ls.append(dlinked)
        
        #2, non-palindrome-2
        dlinked = DLinkedList()
        dlinked.insert_val_before(0, 1)
        dlinked.insert_val_before(1, 2)
        ls.append(dlinked)
        
        #3, palindrome-3
        dlinked = DLinkedList()
        dlinked.insert_val_before(0, 1)
        dlinked.insert_val_before(1, 2)
        dlinked.insert_val_before(2, 1)
        ls.append(dlinked)
        
        #4, non-palindrome-3
        dlinked = DLinkedList()
        dlinked.insert_val_before(0, 1)
        dlinked.insert_val_before(1, 2)
        dlinked.insert_val_before(2, 3)
        ls.append(dlinked)
        
        #5, palindrome-4
        dlinked = DLinkedList()
        dlinked.insert_val_before(0, 1)
        dlinked.insert_val_before(1, 2)
        dlinked.insert_val_before(2, 2)
        dlinked.insert_val_before(3, 1)
        ls.append(dlinked)
        
        #6, non-palindrome-4
        dlinked = DLinkedList()
        dlinked.insert_val_before(0, 1)
        dlinked.insert_val_before(1, 2)
        dlinked.insert_val_before(2, 2)
        dlinked.insert_val_before(3, 3)
        ls.append(dlinked)
        
        return ls
        
    
if __name__ == '__main__':
    unittest.main()