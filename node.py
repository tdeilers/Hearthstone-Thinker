class Node:
    def __init__(self, value, name, cost):
        self.value = value
        self.name = name
        self.cost = cost
        self.amount = 0 
        self.left = None
        self.right = None
        self.leftName = None
        self.rightName = None
        self.outDegree = 0
        self.inDegree = 0
        self.edges = []

    def addEdgeTo(self, node):
        self.edges.append(node)

    def hasEdgeTo(self, otherNode):
        for edge in self.edges:
            if edge is otherNode:
                return True
        return False

    def __str__(self):
        return f'{self.amount}x ({self.cost}) {self.name}'

    def __repr__(self):
        return f'{self.amount}x ({self.cost}) {self.name}'