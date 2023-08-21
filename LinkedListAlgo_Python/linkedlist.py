class Node:
    """Node class for representing individual nodes in the linked list.
    """
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    """"LinkedList class for storing a list of nodes.
    """
    head = None
    count = 0

    def add_at_end(self, data):
        """Adds a node at the end of the list.
        """
        if self.head is None:
            self.head = Node(data, None)
            self.count += 1
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)
        self.count += 1
        return
    
    def add_at_start(self, data):
        """Adds a new node at the start of the list.
        """
        if self.head is None:
            self.head = Node(data, None)
            self.count += 1
            return
        
        node = Node(data, self.head)
        self.head = node 
        self.count += 1
        return

    def remove_from(self, index):
        """Removes a node at the specified index from the list.
        """
        if index < 0 or index > self.list_count():
            raise ValueError("Index out of range")
        
        current_node = self.head
        previous_node = None
        count = 0
        while current_node:
            if count == index - 1:
                # Check if node to be removed is the head
                if index -1 == 0:
                    if current_node.next is None:
                        self.head = None
                        self.count -= 1
                    else:
                        self.head = current_node.next
                        self.count -= 1
                    return

                # If tail is to be removed
                if current_node.next is None:
                    previous_node.next = None
                    self.count -= 1
                else:
                    # Node other than head or tail is to be removed
                    previous_node.next = current_node.next
                    self.count -= 1
                return
            
            previous_node = current_node
            current_node = current_node.next
            count += 1

    def list_count(self):
        """Keeps track of the number of nodes in the list.
        """
        return self.count

    def print_info(self):
        """Prints the nodes in the list.
        """
        current_node = self.head
        linkedlist_data = ""

        while current_node:
            linkedlist_data += f"{current_node.data}-->"
            current_node = current_node.next
        
        return linkedlist_data

    def reverse(self):
        """Reverse the LinkedList.
        """

        previous_node = None

        while self.head != None:
            next_node = self.head.next
            self.head.next = previous_node
            previous_node = self.head
            self.head = next_node
        
        self.head = previous_node

    def find_middle_node(self):
        fast_ptr = self.head
        slow_ptr = self.head
        previous_slow_ptr = slow_ptr

        while (fast_ptr != None) and (fast_ptr.next != None):
            fast_ptr = fast_ptr.next.next
            previous_slow_ptr = slow_ptr
            slow_ptr = slow_ptr.next
        
        # If fast_ptr is None, then list is even
        # If fast_ptr.next is None, then list is odd
        if fast_ptr is None:
            print(f"Middle nodes are {previous_slow_ptr.data} and {slow_ptr.data}")
        else:
            print(f"Middle node is {slow_ptr.data}")
    
    def has_loop(self):
        # Using Floyd's Cycle-Finding Algorithm
        fast_ptr = self.head
        slow_ptr = self.head

        while (fast_ptr != None) and (fast_ptr.next != None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True
        
        return False
    
    def create_loop(self):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        
        # Point the last node's next to the head.
        current_node.next = self.head
