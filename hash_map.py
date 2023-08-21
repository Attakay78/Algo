# HashMap or Dictionary implementation

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
    
    def hash(self, key):
        index = 0
        for character in key:
            index += ord(character)
        
        return index % self.capacity
    
    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            
            index += 1
            index = index % self.capacity
        
        return None
    
    def put(self, key, value):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                pair = Pair(key, value)
                self.map[index] = pair
                self.size += 1

                if self.size >= self.capacity // 2:
                    self.rehash()
                    return
            
            if self.map[index].key == key:
                self.map[index].value = value
                return
            
            index += 1
            index = index % self.capacity
    
    def rehash(self):
        self.size = 0
        self.capacity = self.capacity * 2
        new_map = []

        for _ in range(self.capacity):
            new_map.append(None)
        
        old_map = self.map
        self.map = new_map

        for pair in old_map:
            if pair:
                self.put(pair.key, pair.value)


# Testing
hash_map = HashMap()
hash_map.put("richie", 23)
hash_map.put("george", 15)

print(hash_map.get("richie"))
print(hash_map.get("obed"))
