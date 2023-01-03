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
        Appends the nodes into the list
        If the list it's empty it will make both last and first point to the new node.
        If not empty it will make the next of thenew node points to the present last 
        node and then make  last node point the new node. 
        """
        new_node = Node(data)

        if not self.tail:
            self.tail = new_node
            self.head = self.tail
            self.length += 1
            return 
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return
    

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

    
    