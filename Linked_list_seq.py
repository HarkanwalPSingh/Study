# D.insertfirst(x),D.deletefirst(),D.insertlast(x),D.deletelast()

from typing import List


class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None
        self.prev = None
        # self.prev = None

class ListSequence:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node.val
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])
    
    def __len__(self):
        return self.size

    def insert_first(self,val):
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_last(self,val):
        new_node = ListNode(val)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1  

    def delete_first(self):
        assert self.head
        x = self.head

        self.head = self.head.next
        
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return x

    
    def delete_last(self):
        
        assert self.tail
        x = self.tail

        self.tail = self.tail.prev

        if not self.tail:
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return x

    def swap_ends(self):
        x_first = self.delete_first()
        x_last = self.delete_last()
        self.insert_first(x_last)
        self.insert_last(x_first)
    
    def shift_left(self,k):
        # head - k, k+1 - tail
        # k+1 - tail - head - k
        # Assuming list has atleast k + 2 elements
        
        if (k < 1) or (k > self.size - 1):
            return
        
        x = self.delete_first()
        self.insert_last(x)
        self.shift_left(k - 1)

        


if __name__ == '__main__':

    tests = [('insert_last', 3), ('insert_first', 2), ('insert_last', 8), ('insert_first', 2), ('insert_last', 9), ('insert_first', 7),('swap_ends', ),('shift_left', 3),\
             ('delete_first', ), ('delete_last', )]
    DS = ListSequence()
    for test in tests:
        print(DS)
        if test[0] == 'insert_first':
            x = test[1]
            DS.insert_first(x)
        if test[0] == 'insert_last':
            x = test[1]
            DS.insert_last(x)
        if test[0] == 'swap_ends':
            DS.swap_ends()
        if test[0] == 'delete_first':
            DS.delete_first()
        if test[0] == 'delete_last':
            DS.delete_last()
        if test[0] == 'shift_left':
            k = test[1]
            DS.shift_left(k)
    print(DS)