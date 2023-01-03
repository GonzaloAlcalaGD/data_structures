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

    
    def enqueue(self, data) -> None:
        """
        Queues the nodes into the list
        If the list it's empty it will make both last and first point to the new node.
        If not empty it will make the next of thenew node points to the present last 
        node and then make  last node point the new node. 
        """
        new_node = Node(data)

        if not self.last:
            self.last = new_node
            self.first = self.last
            self.length += 1
            return 
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return