from linkedlist import LinkedList

linked_list = LinkedList()
linked_list.add_at_end(34)
linked_list.add_at_end(35)
linked_list.add_at_end(36)
linked_list.add_at_start(100)

print(linked_list.print_info())
print(linked_list.list_count())
# linked_list.remove_from(4)
# linked_list.remove_from(1)

# print(linked_list.print_info())
# print(linked_list.list_count())

linked_list.reverse()
print(linked_list.print_info())

# linked_list.remove_from(1)

# print(linked_list.print_info())
# print(linked_list.list_count())

linked_list.find_middle_node()
print(linked_list.has_loop())

linked_list.create_loop()
print(linked_list.has_loop())
