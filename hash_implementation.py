class HashTable:
    """
    Python implementation of hash tables.
    """


    def __init__(self, size) -> None:
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
