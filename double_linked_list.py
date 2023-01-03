class Node():

    def __init__(self, data) -> None:
        """
        Initialize the attr of our node.
        """
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList():

    def __init__(self) -> None:
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

        return ' <-> '.join(str(item) for item in nodes)


    def append(self, data) -> None:
        """
        Inserts the node to the last position in the list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return


    def prepend(self, data) -> None:
        """
        Inserts the node to the first position in the list.
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head.prev = new_node
        self.head =  new_node
        self.length += 1 
        return


DLinked = DoubleLinkedList()

DLinked.append(10)
DLinked.append(11)
DLinked.append(12)
DLinked.prepend(9)
DLinked.append(13)

print(DLinked)
print(f'Length: {DLinked.length}')
print(f'Head: {DLinked.head.data}')
print(f'Tail: {DLinked.tail.data}')