class HashTable:
    """
    Python implementation of hash tables.
    """


    def __init__(self, size:int) -> None:
        """
        Initialize propierties of our hash table.
        With a list pre-filled with 'None' values and size 'self.size'.
        """
        self.size = size
        self.data = [None]*self.size

    
    def __str__(self) -> str:
        """
        Returns a string dictionary representation of our hash table.
        """
        return str(self.__dict__)


    def _hash(self, key) -> str:
        """
        Returns the hash of provided object
        """
        return hash(key) % self.size

    
    def set(self, key, value) -> str:
        """
        Set the key-value with the corresponding hash value if hash is not present in our list.
        If the hash exists it appends the value to the corresponding hash
        """
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])
        
        return self.__str__()

    
    def get(self, key):
        """
        Returns the value inside the hashed key in our hash map.
        """
        hash = self._hash(key)
        if self.data[hash]:
            hash_items = len(self.data[hash])
            for keys in range(hash_items):
                if self.data[hash][keys][0] == key:
                    return self.data[hash][keys][1]
        else:
            return None


my_hash = HashTable(4)

print(my_hash.set('grape', 10))
print(my_hash.set('orange', 5))
print(my_hash.get('grape'))
print(my_hash.get('orange'))

