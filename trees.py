class Node():

    def __init__(self, data) -> None:

        self.data = data
        self.left = None
        self.right = None


class Tree():

    def __init__(self) -> None:
        
        self.root = None

    
    def insert(self, data) -> None:
        """
        Inserts the node in the root if the roots it's none
        Otherwise traverses the tree comparing the left and right values.
        """
        node = Node(data)
        current_node = self.root

        if self.root is None:
            self.root = node
            return
        
        while True:
            # Left path
            if data < current_node.data and current_node.left is None: 
                current_node.left = node
                return
            else:
                current_node = current_node.left

            # Right path
            if data > current_node.data and current_node.right is None:
                current_node.right = node
                return
            else:
                current_node = current_node.right