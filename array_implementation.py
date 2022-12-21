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



first_array = MyArray()

first_array.push(1)

print(first_array)