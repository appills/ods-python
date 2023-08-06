from dlinkedlist import DNode, DLinkedList
import unittest

class DLinkedListTest(unittest.TestCase):
    
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
        dlinked = self.get_dlinkedlist()
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
            dlinked.add(i, val)
        return dlinked
        
    def dlinkedlist_palindrome_provider(self):
        ls = []
        #0, palindrome-1
        dlinked = DLinkedList()
        dlinked.add(0, 1)
        ls.append(dlinked)
        
        #1, palindrome-2
        dlinked = DLinkedList()
        dlinked.add(0, 1)
        dlinked.add(1, 1)
        ls.append(dlinked)
        
        #2, non-palindrome-2
        dlinked = DLinkedList()
        dlinked.add(0, 1)
        dlinked.add(1, 2)
        ls.append(dlinked)
        
        #3, palindrome-3
        dlinked = DLinkedList()
        dlinked.add(0, 1)
        dlinked.add(1, 2)
        dlinked.add(2, 1)
        ls.append(dlinked)
        
        #4, non-palindrome-3
        dlinked = DLinkedList()
        dlinked.add(0, 1)
        dlinked.add(1, 2)
        dlinked.add(2, 3)
        ls.append(dlinked)
        
        #5, palindrome-4
        dlinked = DLinkedList()
        dlinked.add(0, 1)
        dlinked.add(1, 2)
        dlinked.add(2, 2)
        dlinked.add(3, 1)
        ls.append(dlinked)
        
        #6, non-palindrome-4
        dlinked = DLinkedList()
        dlinked.add(0, 1)
        dlinked.add(1, 2)
        dlinked.add(2, 2)
        dlinked.add(3, 3)
        ls.append(dlinked)
        
        return ls
        
    
if __name__ == '__main__':
    unittest.main()