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

    
    def pop(self):
        """
        Deletes the last item in the array and returns it.
        """
        if self.length == 0:
            return str('Array\'s length it\'s 0, no item\'s left to pop')
        else:
            last_item = self.data[self.length - 1]
            del self.data[self.length - 1]
            self.length -= 1
            return last_item


    def insert(self, idx, item):
        """
        Inserts element in the desired index.
        """
        if idx > self.length-1:
            print(f'Index: {idx} out of bound. Inserting at the end of the array.')
            self.push(item)
        else:
            print('else')
            self.length += 1
            for index in range(self.length-1, idx, -1):
                self.data[index] = self.data[index-1]
            self.data[idx] = item




first_array = MyArray()

first_array.push(1)
first_array.push(2)
first_array.push(3)
first_array.push(4)




