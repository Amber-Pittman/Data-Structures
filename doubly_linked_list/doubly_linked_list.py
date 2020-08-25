"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
      # create a new_node
      new_node = ListNode(value, None, None)
      # check if the DDL is empty
      if not self.head and not self.tail:
      # if empty assign them to the new node
        self.head = new_node
        self.tail = new_node
        self.length += 1
      #in all other cases
      else:
        # point next to the head
        new_node.next = self.head
        # point self's prev to the new node
        self.head.prev = new_node
        self.head = new_node
        # increment length
        self.length += 1  # or self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # check to see if the head is already empty
        if self.head is None:
          return None
        # otherwise, find the node's value and delete the head
        head_value = self.head.value
        self.delete(self.head)
        # returns the value of the removed Node
        return head_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        # check if the DDL is empty
        if not self.head and not self.tail:
        # if empty assign them to the new node
          self.head = new_node
          self.tail = new_node
          self.length += 1
        #in all other cases
        else:
          # point prev to the tail
          new_node.prev = self.tail
          # point self's next to the new node
          self.tail.next = new_node
          self.tail = new_node
          # increment length
          self.length += 1 


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List. Returns the value of the removed Node."""

    def remove_from_tail(self):
        # check to see if the tail is already empty
        if self.tail is None:
          return None
        # otherwise, find the tail's value and delete the tail
        tail_value = self.tail.value
        self.delete(self.tail)
        # returns the value of the removed tail
        return tail_value

    """Removes the input node from its current spot in the List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # if it's already at the head, do nothing
        if node is self.head:
          return
        # otherwise delete the input node from it's place
        old_value = node.value
        self.delete(node)
        # add the input node to the head
        self.add_to_head(old_value)
        

    """Removes the input node from its current spot in the List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # if it's already at the tail, do nothing
        if node is self.tail:
          return
        # otherwise delete the input node for it's place
        old_value = node.value
        self.delete(node)
        # add the input node to the tail
        self.add_to_tail(old_value)

    """Removes a node from the list and handles cases where the node was the head or the tail"""
    
    def delete(self, node):
        # if both the head and tail is already empty, do nothing
        if self.head is None and self.tail is None:
          return
        # decrement the length since we're deleting a node
        self.length -= 1
        # if the node only has one element, set both head and tail to None
        if self.head == self.tail:
          self.head = None
          self.tail = None
        # if the node is THE head, move the head to the next node before deleting
        elif self.head == node:
          self.head = node.next
          node.delete()
        # or, if the node is THE tail, move the tail back to the previous node before it
        elif self.tail == node:
          self.tail = node.prev
          node.delete()
        # otherwise, just delete the node
        else:
          node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # check to see if the head is already empty
        if self.head is None:
          return None
        # declare head's value
        max = self.head.value
        # set the current node to the head
        current_node = self.head
        # loop through the list with the current node
        while current_node:          
          # if the current node is greater than the max value, set the current node 
          #   to the new max
          if current_node.value > max:
            max = current_node.value
          # keep moving the current node to the next node until it finally reaches None
          current_node = current_node.next
        # When done, return the maximum value in the list
        return max