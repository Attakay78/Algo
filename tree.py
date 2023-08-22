# General Tree Implementation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)
    
    def get_level(self):
        level_count = 0
        parent = self.parent

        while parent:
            level_count += 1
            parent = parent.parent
        
        return level_count

    def print_tree(self):
        level = self.get_level()

        if level == 0:
            print(self.data)
        else:
            spaces = " " * level * 3
            print(f"{spaces}|___{self.data}")

        for child in self.children:
            child.print_tree()


# Binary Tree Implementation
class BiTreeNode(TreeNode):
    def add_child(self, child):
        if len(self.children) < 2:
            child.parent = self
            self.children.append(child)


if __name__ == "__main__":
    electronics = TreeNode("Electronics")
    phone = TreeNode("Phone")
    laptop = TreeNode("Laptop")

    electronics.add_child(phone)
    electronics.add_child(laptop)

    iphone = TreeNode("Iphone")
    samsung = TreeNode("Samsung")
    nokia = TreeNode("Nokia")

    phone.add_child(iphone)
    phone.add_child(samsung)
    phone.add_child(nokia)

    toshiba = TreeNode("Toshiba")
    dell = TreeNode("Dell")

    laptop.add_child(toshiba)
    laptop.add_child(dell)

    electronics.print_tree()
