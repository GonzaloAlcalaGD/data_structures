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
    

    