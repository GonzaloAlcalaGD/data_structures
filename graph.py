class Graph:

    def __init__(self) -> None:
        self.n_of_nodes = 0
        self.adjacent_list = {}
    

    def __str__(self) -> str:
        return str(self.__dict__)
    

    def add_vertex(self, node) -> None:
        """
        Adds a vertex into our adjacent list
        """
        self.adjacent_list[node] = []
        self.n_of_nodes += 1
        return
    

    def add_edge(self, node_1, node_2) -> None:
        """
        Adds a edge into the desired node
        """
        self.adjacent_list[node_1].append(node_2)
        self.adjacent_list[node_2].append(node_1)
        return

    
    def show_connections(self) -> None:
        """
        Prints the current connections in our graph
        """

        for vertex, neighbor in self.adjacent_list.items():
            print(str(vertex), end=' ---> ')
            print(' '.join(str(neighbor)))


myGraph = Graph()

myGraph.add_vertex(0)
myGraph.add_vertex(1)
myGraph.add_vertex(2)
myGraph.add_vertex(3)
myGraph.add_vertex(4)
myGraph.add_vertex(5)
myGraph.add_vertex(6)
myGraph.add_edge(3, 1)
myGraph.add_edge(3, 4)
myGraph.add_edge(4, 2)
myGraph.add_edge(4, 5)
myGraph.add_edge(1, 2)
myGraph.add_edge(1, 0)
myGraph.add_edge(0, 2)
myGraph.add_edge(6, 5)
print(myGraph)
myGraph.show_connections()