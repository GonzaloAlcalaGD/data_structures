class Node():

    def __init__(self, data) -> None:

        self.data = data
        self.next = None

class Queue():


    def __init__(self) -> None:
        
        self.first = None
        self.last = None
        self.length = 0
    

    def peek(self) -> Node:
        """
        Returns the first node from our queue
        """
        return

    
    def enqueue(self, data) -> None:
        """
        Enqueues the node into the last position of our queue
        """
        node = Node(data)

        if self.first is None:
            self.first = node
            self.last = self.first
            self.length += 1
            return
        else:
            self.last.next = node
            self.last = node
            self.length += 1
            return

    
    def dequeue(self) -> None:
        """
        Dequeues the first node in our queue
        """
        return
    

    def is_empty(self) -> bool:
        """
        Returns true if the queue it's empty otherwise false.
        """
        if self.first is None:
            return True
        else:
            return False