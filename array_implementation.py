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


first_array = MyArray()

print(first_array)