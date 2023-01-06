import logging

logging.basicConfig(level=logging.DEBUG)

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
            if data < current_node.data:
                if current_node.left is None: 
                    current_node.left = node
                    return
                else:
                    current_node = current_node.left

            # Right path
            if data > current_node.data:
                 if current_node.right is None:
                    current_node.right = node
                    return
                 else:
                    current_node = current_node.right


    def traverse(self, current_node) -> None:
        """
        Traverses over the tree if the next node in the tree is not None
        """

        if current_node is not None:
            self.traverse(current_node.left)
            print(current_node.data)
            self.traverse(current_node.right)
            

        
    def print_tree(self) -> None:
        """
        Calls a recursive function to print the next node in the tree
        """

        if self.root is not None:
            self.traverse(self.root)
        else:
            return logging.info('Tree its empty')
    

    def lookup(self, data) -> Node:
        """
        Traverses the Tree looking for the node, if it exist returns True
        otherwhise returns False
        """
        current_node = self.root

        while True:

            if current_node is None:
                return False
            
            if current_node.data == data:
                return True
            
            if data < current_node.data: # Left path
                current_node = current_node.left
            else:
                current_node = current_node.right # Right path
    
        


binaryTree = Tree()

binaryTree.insert(10)
binaryTree.insert(5)
binaryTree.insert(6)
binaryTree.insert(12)
binaryTree.insert(8)

binaryTree.print_tree()