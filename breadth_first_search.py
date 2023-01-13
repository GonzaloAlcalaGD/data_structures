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
        Traverses the Tree looking for the node, if it exist returns the actual Node
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

            if data > current_node.data:
                current_node = current_node.right # Right path

    
    def remove(self, data) -> Node:
        """
        Traverses the Tree looking for the desired Node and removes it 
        And reconfigures both child and parent nodes if needed.
        """
        current_node = self.lookup(data)
        parent_node = None

        while current_node:
            
            # Find the node and his parent node
            if data < current_node.data: # Left path
                parent_node = current_node
                current_node = current_node.left

            if data > current_node.data:
                parent_node = current_node
                current_node = current_node.right # Right path
            
            if data == current_node.data:

                # Option 1 - No right child
                if current_node.right is None:

                    if parent_node is None:
                        self.root = current_node.left
                    
                    #If the parent it's greather than our current node, make our current node left a child a child of parent.
                    if parent_node.data > current_node.data:
                        parent_node.left = current_node.left 
                    
                    # If the parents it's lesser than our current node, make our current node left a child a right child of parent
                    if parent_node.data < current_node.data:
                        parent_node.right = current_node.left
                
                # Option 2 - Right child without left child
                elif current_node.right.left is None:

                    current_node.right.left = current_node.left

                    if parent_node.left is None:
                        self.root = current_node.right
                    
                    # If parent is greather than our current node, make our current right a child of the left the parent
                    if parent_node.data > current_node.data:
                        parent_node.left = current_node.right
                    
                    # If parent is lesser than our currend node, make our current right a child of the right 
                    if parent_node.data < current_node.data:
                        parent_node.right = current_node.right
                    
                # Option 3 - Right child that has a left child
                else:
                    
                    left_most = current_node.right.left
                    left_most_parent = current_node.right

                    while left_most is not None:
                        left_most_parent = left_most
                        left_most = left_most.left
                    
                    #Parent's left subtree is now leftmost's right subtree
                    left_most_parent.left = left_most.left
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node is None:
                        self.root = left_most
                    
                    if current_node.data < parent_node.data:
                        parent_node.left = left_most
                    
                    if current_node.data > parent_node.data:
                        parent_node.right = left_most

            return True


    def breadthFirstSearchR(self, queue, list=[]) -> list:
        
        if not len(queue): # If queue it's empty we return empty list
            return list
        
        current_node = queue[0]
        del queue[0]
        list.append(current_node.data)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

        
        return self.breadthFirstSearchR(queue, list)

        
    
        


binaryTree = Tree()

binaryTree.insert(9)
binaryTree.insert(4)
binaryTree.insert(6)
binaryTree.insert(20)
binaryTree.insert(170)
binaryTree.insert(15)
binaryTree.insert(1)

print(binaryTree.breadthFirstSearchR([binaryTree.root], []))