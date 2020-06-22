"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

"""

# - Has the methods: `enqueue`, `dequeue`, and `len`.
#   - `enqueue` adds an element to the back of the queue.
#   - `dequeue` removes and returns the element at the front of the queue.
#   - `len` returns the number of elements in the queue.


# Implementation using arrays
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         return self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             return self.storage.pop(0)


# Implementation using linked lists
class Node:
  def __init__(self, value=None, next_node=None):
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

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        #checking to see if this is equal to None
        new_node = Node(value)
        # this is if we have an empty list
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # if we DO have a head in the list
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            # if list empty do nothing - return nothing
            return None

        # if head has no next, there is a single element in the LL. 
        if not self.head.get_next():
            # get a reference to the head 
            head = self.head
            # point head and tail to none since there's only one element in the LL
            self.head = None 
            self.tail = None

            return head.get_value()

        # If there is a head and there are TWO OR MORE items in the LL, get the head's value
        value = self.head.get_value()
        # Now we get the value of the current head and reset the head to the next node (pointer)
        self.head = self.head.get_next()
        # And then we return the value
        return value

    def contains(self, value):
        if not self.head:
            return False
        # Get a ref to the node we're currently at; update this as we traverse
        current = self.head
        # Check to see if we're at a valid node
        while current:
            # Return True if the current value we're looking for matches our target value
            if current.get_value() == value:
                return True 
            # update our current node to the current node's next_node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_length(self):
        temp = self.head
        count = 0

        while (temp):
            count += 1
            temp = temp.next_node
        return count

    def get_max(self):
        if self.head is None:
            return self.head

        current_node = 0
        next_n = self.head.next_node

        while self.head is not None:
            if current_node <= next_n.value:
                current_node = next_n.value
            self.head = self.head.next_node

        return current_node


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.storage.get_length()

    def enqueue(self, value):
        return self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_head()


