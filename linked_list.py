import logging

logging.basicConfig(level=logging.DEBUG)

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
        self.head = None
        self.tail = None
        self.length = 0


    def __repr__(self) -> str:
        """
        Prints the current nodes in our list.
        """
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        nodes.append('None')
        return str(' -> '.join(nodes))
    

    def append(self, data) -> None:
        """
        Inserts the node to the first position in the list.
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    

    def dequeue(self) -> None:
        """
        If the list it's empty it will return the apropiate message.
        If not, it will simply move the self.first to the next node in the queue.
        """
        if not self.tail:
            logging.info('Queue empty.')
            return
        if self.tail == self.head:
            self.tail = None
        self.head = self.head.next
        self.length -= 1
        return

    
    