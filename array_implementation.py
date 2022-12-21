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
            print(f'Index: {idx} out of bound. Inserting at the end of the array.') # This is not Javascript for god's sake
            self.push(item)
        else:
            print('else')
            self.length += 1
            for index in range(self.length-1, idx, -1):
                self.data[index] = self.data[index-1]
            self.data[idx] = item
    

    def delete(self, idx):
        if idx < 0 or idx >= self.length:
            return str(f'Index out of bounds can\'t access index: {idx}')
        else:     
            for index in range(idx, self.length-1):
                self.data[index] = self.data[index+1]
            del self.data[self.length-1]
            self.length -= 1



