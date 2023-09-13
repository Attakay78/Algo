class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def add_child(self, child_node):
        if child_node == self.data:
            return
        
        if child_node > self.data:
            if self.right_child:
                self.right_child.add_child(child_node)
            else:
                self.right_child = BSTNode(child_node)
       
        if child_node < self.data:
            if self.left_child:
                self.left_child.add_child(child_node)
            else:
                self.left_child = BSTNode(child_node)
    
    def in_order_traversal(self, elements=[]):

        if self.left_child:
            elements = self.left_child.in_order_traversal(elements=elements)
        
        elements.append(self.data)

        if self.right_child:
            elements = self.right_child.in_order_traversal(elements=elements)
        
        return elements
    
    def search(self, data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left_child:
                return self.left_child.search(data)
            else:
                return False
        
        if data > self.data:
            if self.right_child:
                return self.right_child.search(data)
            else:
                return False
    
    def find_min(self):
        if self.left_child:
            return self.left_child.find_min()
        
        return self.data
    
    def find_max(self):
        if self.right_child:
            return self.right_child.find_max()
        
        return self.data
    
    def calculate_sum(self, sum=0):
        sum += self.data

        if self.left_child:
            sum = self.left_child.calculate_sum(sum=sum)
        
        if self.right_child:
            sum = self.right_child.calculate_sum(sum=sum)
        
        return sum


def build_tree(elements):
    root = BSTNode(elements[0])

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
    # print(root.pre_order_traversal())
    # print(root.post_order_traversal())