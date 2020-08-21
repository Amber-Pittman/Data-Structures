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
class Node():
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._nodes = None
    
    def __str__(self):
        output = ""
        current_node = self.head
        while current_node is not None:
            output += f"{current_node.value}"
            current_node = current_node.next_node
        return output

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def remove_tail(self):
        current = self.head
        if self.head is None:
            return None
        while current is not None:
            if current.next_node == self.tail:
                self.tail = current
                return current
        return current.value

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
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
        next_node = self.head.next_node

        while self.head is not None:
            if current_node <= next_node.value:
                current_node = next_node.value
            self.head = self.head.next_node
        
        return current_node


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
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
        node = self.storage.remove_head()
        return node

new_stack = Stack()
# new_stack.push(5)
# new_stack.push(6)
# new_stack.push(7)
# new_stack.push(8)
# new_stack.push(9)
# new_stack.push(10)

print(new_stack.pop())
print(new_stack.pop())
print(new_stack.__len__())
