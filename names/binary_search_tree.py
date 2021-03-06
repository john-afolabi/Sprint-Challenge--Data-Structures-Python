class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_value = self.value

        if curr_value == target:
            return True

        if target < curr_value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)

        if target > curr_value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Recursive
        if self.value is not None:
            cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)
