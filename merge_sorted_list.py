# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    head = None

    def append(self, data):
        if self.head is None:
            self.head = ListNode(val=data)
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = ListNode(val=data)
        return

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        linked_list = LinkedList()

        if node1 is None and node2 is None:
            return None

        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                linked_list.append(node1.val)
                node1 = node1.next
            else:
                linked_list.append(node2.val)
                node2 = node2.next

        if node1 is not None:
            while node1 is not None:
                linked_list.append(node1.val)
                node1 = node1.next

        if node2 is not None:
            while node2 is not None:
                linked_list.append(node2.val)
                node2 = node2.next

        return linked_list.head
