class Node():
    """
    Node implementation in Python.
    """


    def __init__(self, data) -> None:
        """
        Initialize attributes of our Node.
        """
        self.data = data
        self.next = None


class Queue():
    """
    Queue implementation in Python.
    """


    def __init__(self) -> None:
        """
        The 'first' attribute points at the front of the Queue (First element entered).
        The 'last' attribute points at th end of the Queue (Last element entered).
        """
        self.first = None
        self.last = None
        self.length = 0