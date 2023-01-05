class Node():

    def __init__(self, data) -> None:

        self.data = data
        self.next = None

class Queue():


    def __init__(self) -> None:
        
        self.first = None
        self.last = None
        self.length = 0
    

    def __repr__(self):

        node = self.first
        

        while node is not None:
            print(node.data)
            print('↑')
            node = node.next
        
        return 'None'


    def peek(self) -> Node:
        """
        Returns the first node from our queue
        """
        if  self.is_empty():
            return 'Queue it\'s empty'
        else:
            return self.first.data
            
    
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
        holder = self.first.next

        if holder is None:
            self.first = None
            self.length -= 1
            return
        else:
            self.first.next = None
            self.first = holder
            self.length -= 1
            return


    def is_empty(self) -> bool:
        """
        Returns true if the queue it's empty otherwise false.
        """
        if self.first is None:
            return True
        else:
            return False

my_Queue = Queue()

for i in range(5):
    my_Queue.enqueue(i)

print(f'First: {my_Queue.peek()}')
print(my_Queue)
my_Queue.dequeue()
print(f'First: {my_Queue.peek()}')
print(my_Queue)