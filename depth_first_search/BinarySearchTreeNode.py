from Node import Node
class BinarySearchTreeNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None
        self.neighbors = [self.left, self.right]
        self.visited = False

    def add_left(self, node):
        """Add a left child node if value is less than current node."""
        if node.value < self.value:
            self.left = node
            self.neighbors[0] = node
            return True
        return False

    def add_right(self, node):
        """Add a right child node if value is greater than current node."""
        if node.value > self.value:
            self.right = node
            self.neighbors[1] = node
            return True
        return False

    def add_child(self, node):
        """Add a child node to the correct position in the BST."""
        if node.value < self.value:
            return self.add_left(node)
        elif node.value > self.value:
            return self.add_right(node)
        return False