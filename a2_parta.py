#    Main Author(s): Shayan Ramezanzadeh, Babak Ghafourigivi
#    Main Reviewer(s): Ashkan Rahimpour Harris

class HashTable:
    # Initialize the hash 
    # default capacity: 32
    def __init__(self, cap=32):
        self._capacity = cap
        self.size = 0
        self.table = [None] * self._capacity
    
    # Hash function that calculates index according to the given key
    def _hash(self, key):
        return hash(key) % self._capacity

    # Resize hash table if load factor exceeds a threshold 
    def _resize(self):
        old_table = self.table
        self._capacity = self._capacity * 2
        self.table = [None] * self._capacity
        self.size = 0

        # Reinsert valid items in new table
        for item in old_table:
            if item and item != "TOMBSTONE":
                self.insert(item[0], item[1])

    # Insert new key and value pair in hash table
    def insert(self, key, value):
        # Prevent duplicate keys
        if self.search(key) is not None:
            return False

        # Check if resizing is necessary 
        if (self.size + 1) / self._capacity > 0.7:
            self._resize()

        idx = self._hash(key)
        # Handle collisions using linear probing
        while self.table[idx] is not None and self.table[idx] != "TOMBSTONE":
            idx = (idx + 1) % self._capacity

        self.table[idx] = (key, value)
        self.size += 1
        return True

    # Modify the value with existing key
    def modify(self, key, value):
        idx = self._hash(key)
        # Loop to handle collisions
        for _ in range(self._capacity):
            if self.table[idx] is None:# Key not found
                return False
            if self.table[idx] != "TOMBSTONE" and self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return True
            idx = (idx + 1) % self._capacity
        return False # Key not found after probing

    # Remove a key and value pair from hash table
    def remove(self, key):
        idx = self._hash(key)
        # Loop to handle collisions
        for _ in range(self._capacity):
            if self.table[idx] is None:# Key not found
                return False
            if self.table[idx] != "TOMBSTONE" and self.table[idx][0] == key:
                self.table[idx] = "TOMBSTONE"
                self.size -= 1
                return True
            idx = (idx + 1) % self._capacity
        return False # Key not found after probing

    # Search for key and return its value
    def search(self, key):
        idx = self._hash(key)
        # Loop to handle collisions
        for _ in range(self._capacity):
            if self.table[idx] is None: # Key not found
                return None
            if self.table[idx] != "TOMBSTONE" and self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self._capacity
        return None # Key not found after probin

    # Return current capacity of hash table
    def capacity(self):
        return self._capacity

    # Return number of elements in hash table
    def __len__(self):
        return self.size
