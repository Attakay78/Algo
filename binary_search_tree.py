class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        # left_tree: node : right_tree
        elements = []

        # Check if there is a left tree then traverse the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Add the current node (which should be the middle node)
        elements.append(self.data)

        # Check if there is a right tree then traverse the right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self, data):
        # Search for data in the tree
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        
        return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        
        return self.data
    
    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()

        sum += self.data

        if self.right:
            sum += self.right.calculate_sum()
        
        return sum
    
    def pre_order_traversal(self):
        # node : left_tree : right_tree
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        # left_tree: right_tree : node
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for element in elements[1:]:
        root.add_child(element)
    
    return root


if __name__ == "__main__":
    tree_data = [23, 7, 9, 27, 34, 5, 6, 10, 15, 11, 43]
    root = build_tree(tree_data)
    print(root.in_order_traversal())
    print(root.search(51))
    print(root.find_min())
    print(root.find_max())
    print(root.calculate_sum())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
