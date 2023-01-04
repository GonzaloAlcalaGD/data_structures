class Node():

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.length = 0


class Stack():

    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0