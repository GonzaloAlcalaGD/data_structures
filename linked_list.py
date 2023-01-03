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


class LinkedList():
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

        return ' -> '.join(str(item) for item in nodes)
    

    def __iter__(self) -> None:
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def prepend(self, data) -> None:
        """
        Inserts the node to the first position in the list.
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        self.length += 1

        return

    
    def append(self, data) -> None:
        """
        Inserts the node to the last position in the list.
        """
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        
        for current_node in self:
            pass
        current_node.next = new_node

        return
    

    
myList = LinkedList()
myList.append(10)
myList.append('b')
myList.append(11)
myList.prepend(9)
myList.prepend('a')
myList.append(12)
myList.prepend(8)
print(myList)