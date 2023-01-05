class Node():

    def __init__(self, data) -> None:

        self.data = data
        self.next = None

class Queue():


    def __init__(self) -> None:
        
        self.first = None
        self.last = None
        self.length = 0