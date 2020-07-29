"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList


class Stack():
    
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        
        
    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        

        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()


        
            

"""
        current = self.head
        count = 0
        
        
        if not self.head:
            return count
        
        
        while current.next is not None:
            count+=1
            current = current.get_next()
        return count
        
        #return len(self.storage)
"""

newstack = Stack()

newstack.push(100)
newstack.push(101)
newstack.push(105)

print(newstack.pop())
print(len(newstack))

print(newstack.pop())
print(len(newstack))
print(newstack.pop())
print(len(newstack))





"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        while len(self.storage) > 0:
            return self.storage.pop()
        return None
"""
"""
    def push(self,value):
        self.storage.add_to_head(value)
        
        new_stack = Node(value,None)
        
        if not self.head:
            self.size += 1
            self.head = new_stack
            self.tail = new_stack
        else:
            self.size += 1
            self.head.set_next(new_stack)
            self.head = new_stack
    """

