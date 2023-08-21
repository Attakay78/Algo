# HashMap or Dictionary implementation

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.storage = [None, None]
    
    def hash(self, key):
        # Calculate hash of the key using ord method
        ascii_sum = 0
        for char in key:
            ascii_sum += ord(char)
        return ascii_sum % self.capacity
    
    def rehash(self):
        # Rehash every key in the HashMap
        self.size = 0
        self.capacity = self.capacity * 2

        old_storage, self.storage = self.storage, [None] * self.capacity

        # Put all pairs in old storage into new storage with bigger capacity
        for pair in old_storage:
            if pair:
                key, value = pair.key, pair.value
                self.put(key, value)
    
    def put(self, key, value):
        hash_index = self.hash(key)

        # Loop till we get empty space to insert Pair
        while True:
            if self.storage[hash_index] == None:
                pair = Pair(key, value)
                self.storage[hash_index] = pair
                self.size += 1

                # Rehash all keys since size of storage is >= capacity
                if self.size >= self.capacity // 2:
                    self.rehash()
                    return
            
            # To prevent key duplication, Just change the value
            if self.storage[hash_index].key == key:
                self.storage[hash_index].value = value
                return
            
            # Recompute hash_index to prevent index from going out of
            # bound with the capacity value, resets hash_index to first 
            # index in storage
            hash_index += 1
            hash_index = hash_index % self.capacity
    
    def get(self, key):
        hash_index = self.hash(key)
        
        while self.storage[hash_index] != None:
            if self.storage[hash_index].key == key:
                return self.storage[hash_index].value
            
            # Recompute hash_index to prevent index from going out of
            # bound with the capacity value, resets hash_index to first 
            # index in storage
            hash_index += 1
            hash_index = hash_index % self.capacity

        return None


# Testing
hash_map = HashMap()

hash_map.put("Name", "Kofi")
hash_map.put("Age", 3)
hash_map.put("Salary", "2500")
hash_map.put("Position", 'Senior Engineer')

print(hash_map.get("Name"))
print(hash_map.get("Age"))
print(hash_map.get("Salary"))
print(hash_map.get("Position"))
print("********************************")

# Print HashMap
for val in hash_map.storage:
    if val != None:
        print(val.key, val.value)
    else:
        print(val)
