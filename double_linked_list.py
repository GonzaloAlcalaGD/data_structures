class Node():

    def __init__(self, data) -> None:
        """
        Initialize the attr of our node.
        """
        self.data = data
        self.next = None
        self.previous = None


class DoubleLinkedList():

    def __init__(self) -> None:
        self.head = None
        self.tail = None