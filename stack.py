class Node():

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack():

    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
    

    def __iter__(self) -> None:
        """
        Iterates over the Stack
        """
        node = self.top

        while node is not None:
            yield node
            node = node.next


    def __repr__(self) -> None:
        """
        Represents our Stacks as a string.
        """
        node = self.top
        

        while node is not None:
            print(node.data)
            print('↓')
            node = node.next
        
        return 'None'

    def peek(self) -> Node:
        """
        Returns the first node in the stack
        """
        if self.length == 0:
            return 'Stack it\'s empty'
        else:
            return self.top.data
    

    def push(self, data) -> str:
        """
        Adds a node into the top of the stack
        """
        new_node = Node(data)

        if self.top is None:
            self.bottom = new_node
            self.top = self.bottom
            self.length += 1
            return f'Node with data {data} successfully allocated at the top of the stack'

        new_node.next = self.top
        self.top = new_node
        self.length += 1

        return  f'Node with data: {data} successfully allocated at the top of the stack'


    def pop(self) -> Node:
        """
        Removes and returns the top node in the stack
        """
        pass

    
    def is_empty(self) -> bool:
        """
        Returns true if the stack it's empty or false if is not.
        """
        if self.length == 0:
            return True
        else:
            return False


my_stack = Stack()

for i in range(5):
    print(my_stack.push(i))

# print(my_stack.is_empty())
# print(my_stack)
# print(my_stack.top.data)