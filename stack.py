class Node():

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack():

    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0