# 1->56-> 57->

# 1->6-2->5->

# 1->
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head = None

    def add_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = Node(data)
        return

    def print_info(self):
        if self.head is None:
            return
        
        current_node = self.head
        linked_list = ""

        while current_node is not None:
            linked_list += f"{current_node.data}->"
            current_node = current_node.next
        
        return linked_list
    
    def add_at_start(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        node = Node(data)
        node.next = self.head
        self.head = node
        return

    def remove_at(self, index):
        pass
