class Node:
    def __init__(self,value = None, next_node = None):
        self.value = value
        self.next_node = next_node
        
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next    

   


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
  
    def add_to_tail(self,value):
        new_node = Node(value,None)
        self.length += 1
        
        if not self.head:
        
            self.head = new_node
            self.tail = new_node
        
        else:
        
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self,value):
        
        new_node = Node(value,None)
        self.length +=1
        
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove_head(self):

        if not self.head:
            return None
        if not self.head.get_next():
            #print('no such thing as get_next()')
            head = self.head
            self.head = None
            self.tail = None
            
            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        self.length -= 1
        return value

    

    def contains(self,value):
        if not self.head:
            return False

        current = self.head

        while current:

            if current.get_value() == value:
                return True
            current = current.get_next()

        return False

    def get_max(self):
        
        current = self.head
        
        if not self.head:
            return None
        
        else:
            maximum = current.get_value()
            while current:
                if maximum < current.get_value():
                    maximum = current.get_value()
                current = current.get_next()
            return maximum
    
    def length(self):
        return self.length
    #def delete(self):

#make sure the list isn't empty
        #if there's only one value, return that value
        #cycle through list, set first value to MAX
        # compare MAX to the next value, if MAX < next value, next value = max
        # while not null, continue
        # when null return max        
        
         
new_list = LinkedList()         
new_list.add_to_head(3)
new_list.add_to_head(44)
print(new_list.head.value)
print(new_list.head.get_next().value)

"""
new_list.add_to_head(1)
new_list.add_to_tail(7)
new_list.add_to_head(88)
print(new_list.head.value)
print(new_list.length)
print(new_list.tail.get_next())
print(new_list.length)
print(new_list.head.get_next())
#print(new_list.head.get_next().value)
new_list.remove_head()
"""



