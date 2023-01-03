class Node():

    def __init__(self, data) -> None:
        """
        Initialize the attr of our node.
        """
        self.data = data
        self.next = None
        self.previous = None