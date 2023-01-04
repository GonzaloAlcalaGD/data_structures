class Node():

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack():

    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
    

    def peek(self) -> Node:
        """
        Returns the first node in the stack
        """
        pass
    

    def push(self, data) -> Node:
        """
        Adds a node into the top of the stack
        """
        pass


    def pop(self) -> Node:
        """
        Removes and returns the top node in the stack
        """
        pass

    
    def is_empty(self) -> bool:
        """
        Returns true if the stack it's empty or false if is not.
        """
        pass