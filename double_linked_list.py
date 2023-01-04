import logging

logging.basicConfig(level=logging.DEBUG)

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

    
    def traverse_to_index(self, idx) -> Node:
        """
        Traverses the list and return the desired node
        """
        current_node = self.head
        count = 0

        while count != idx:
            current_node = current_node.next
            count += 1
        
        return current_node

    
    def insert(self, idx, data) -> None:
        """
        Insert's the node at the desired idx location.
        """
        new_node = Node(data)

        if idx < 0 or idx >= self.length:
            logging.warning(f'Invalid index: {idx} for node with data: {data} ')
            return

        if idx == 0:
            self.prepend(data)
            return
        
        if idx == self.length-1:
            self.append(data)
            return
        else:
            leader = self.traverse_to_index(idx-1)
            holder = leader.next
            leader.next = new_node
            holder.prev = new_node
            new_node.next = holder
            new_node.prev = leader
            self.length += 1
            return


    def remove(self, idx) -> None:
        """
        Removes the desired node at the index position
        """

        if idx < 0 or idx >= self.length:
            logging.warning(f'Invalid index: {idx} ')
            return

        if idx == 0:
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return
        
        if idx == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        else:
            leader = self.traverse_to_index(idx-1)
            unwanted_node = leader.next
            holder = unwanted_node.next
            leader.next = holder
            holder.prev = leader
            self.length -= 1
            return

DLinked = DoubleLinkedList()

DLinked.append(10)
DLinked.append(11)
DLinked.append(12)
DLinked.prepend(9)
DLinked.append(13)
DLinked.insert(4, 100)
DLinked.insert(5, 101)
DLinked.insert(0, 102)
DLinked.remove(idx=7)
print(DLinked)
print(f'Length: {DLinked.length}')
print(f'Head: {DLinked.head.data}')
print(f'Tail: {DLinked.tail.data}')
