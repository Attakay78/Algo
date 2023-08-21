class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        parent = self.parent
        level = 0

        while parent:
            parent = parent.parent
            level += 1
        
        return level

    def print_tree(self, level = None):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|___" if self.parent else ""

        if level and self.get_level() <= level:
            print(prefix + self.data)

            for child in self.children:
                child.print_tree(level)


class BiTreeNode(TreeNode):
    def add_child(self, child):
        if len(self.children) < 2:
            child.parent = self
            self.children.append(child)
