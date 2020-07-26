"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        if node is not None:
            self.length = 1
        else:
            self.length = 0
        #self.length = 1 if node is not None else 0
        #self.length = 0
    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            self.delete(node)
            #self.length -= 1 no longer needed due to new delete func
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        """
        check the list to see if it's empty > if empty return 

        check to see if the node selected is the head of the list
        >if the node is the head, set self.head to node.next

        check to see if the node is the tail
        >if the node is the tail, set self.tail to node.prev

        if the node is somewhere in the middle
        if node.next is not None
        node.
        """
        """
        current = self.head
        node_deleted = False

        if current is None:
            node_deleted = False
        
        elif current.value == node:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        
        elif self.tail.value == node:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.value == node:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.length -= 1
        
        """
        deleted = False
        if self.head is None or node is None:
            
            return None
        
        if self.head == node:
            #self.length -= 1
            self.head = node.next
            deleted = True
        if self.tail == node:
            #self.length -= 1
            self.tail = node.prev    
            deleted = True
        if node.next is not None:
            #self.length -= 1
            node.next.prev = node.prev
            deleted = True
        if node.prev is not None:
            #self.length -= 1
            node.prev.next = node.next
            deleted = True
        
        if deleted == True:
            self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        
        maximum = None
        current = None

        current = maximum = self.head
        while current:
            if current.value > maximum.value:
                maximum = current
            current = current.next
        return maximum.value   



DLL = DoublyLinkedList()
print(DLL.delete(DLL.head))
DLL.add_to_head(2)
DLL.add_to_head(1)
DLL.add_to_tail(3)

print(DLL.head.value)
print(DLL.tail.prev.value)
print(DLL.tail.value)
print('DLL Length')
print(len(DLL))
print('DLL current head')
print(DLL.head.value)
DLL.delete(DLL.head)
print('DLL head after delete')
print(DLL.head.value)
print('DLL length after delete')
print(len(DLL))
print('getmax of DLL')
print(DLL.get_max())

