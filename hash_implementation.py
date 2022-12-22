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
        return hash(key)


my_hash = HashTable(4)

print(my_hash._hash('grape'))
print(my_hash)