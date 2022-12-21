class MyArray():
    """
    Array implementation
    """

    def __init__(self) -> None:
        """
        Initialize array length to 0
        Initialize the data of the array with a dict:
            key -> index
            value -> value
        """
        self.length = 0
        self.data = {}

    
    def __str__(self) -> str:
        """
        Return the attributes of the class in a dictionary format
        """
        return str(self.__dict__)


    def push(self, item) -> None:
        """
        Adds item to the end of the array
        """
        self.length += 1
        self.data[self.length - 1] = item


    def get(self, idx):
        """
        Returns element inside the index provided.
        If index doesn't exist returns out of bound error message.
        """
        if self.data.get(idx):
            return self.data[idx]
        else:
            return str(f'Out of bound error, index : {idx} doesn\'t exist inside the array')


first_array = MyArray()


print(first_array)


