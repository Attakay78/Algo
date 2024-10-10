# LRUCache using Doubly LinkedList
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.node_lookup = {}
        self.LRU_CACHE_SIZE = capacity
    
    def move_to_start(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.head.previous = node
        node.next = self.head
        node.previous = None
        self.head = node
        return
    
    def remove_node(self, node=None):
        if node is not None:
            previous_node = node.previous
            next_node = node.next
            previous_node.next = next_node
            next_node.previous = previous_node
            return
        
        tail = self.tail
        self.tail = tail.previous
        self.tail.next = None

        del self.node_lookup[tail.key]
        return

    def put(self, key, value):
        if key in self.node_lookup:
            node = self.node_lookup[key]
            node.value = value
            self.move_to_start(node)
            return
        
        node = Node(key, value)
        self.node_lookup[key] = node
        self.move_to_start(node)

        if len(self.node_lookup) > self.LRU_CACHE_SIZE:
            self.remove_node()
        return

    def get(self, key):
        if key in self.node_lookup:
            node = self.node_lookup[key]
            self.remove_node(node)
            self.move_to_start(node)
            return node.value
        
        return -1


from collections import OrderedDict

# LRUCache using OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.items.keys():
            self.items.move_to_end(key, last=False)
            return self.items[key]
        
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.items.keys():
            self.items[key] = value
            self.items.move_to_end(key, last=False)
            return
        
        self.items[key] = value
        self.items.move_to_end(key, last=False)

        if len(self.items) > self.capacity:
            self.items.popitem(last=True)
        
        return


cache = LRUCache(5)

for i in range(5):
    cache.put(str(i), i)

cache.get("4")
cache.get("4")
cache.put("3", 7)
cache.put("1", 2)
cache.put("6", 9)
print(cache.items.items())
