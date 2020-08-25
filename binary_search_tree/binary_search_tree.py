"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # is the value less than the Node's value?
        if value < self.value:
            # if no left value set the left to the new node
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # if left already taken, insert the left into a new node with a new value
                self.left.insert(value)
        #is the value more than the Node's value?
        if value >= self.value:
            #if no right value, set the right to the new node
            if self.right is None:
                self.right = BSTNode(value)
            else:
                #if right already taken, insert the right into a new node with a new value
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check if the value is the same as the target already
        if self.value == target:
            return True
        #otherwise, declare that it has not been found yet
        found = False
        #compare target to the current value
        if self.value >= target:
            # is it in the left subtree?
            if self.left is None:
                return False
            found = self.left.contains(target)
        if self.value < target:
            # is it in the right subtree?
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found 

    # Return the maximum value found in the tree
    def get_max(self):
        # largest values always go to the right
        if self.right is None:
            # if we can't go right, return the current value
            return self.value
        # if we know we can go to the right, call get max on the right and return it
        max = self.right.get_max()
        return max 

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)

        fn(self.value)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  