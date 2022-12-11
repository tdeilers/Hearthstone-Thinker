from node import Node

class AVL:
    def __init__(self):
        self.root = None
        self.rootName = None

    def getBalance(self, node): 
        return self.heightHelper(node.right) - self.heightHelper(node.left)

    def balance(self, node):
        if node is not None:
            bal = self.getBalance(node)

            if bal >= 2: 

                # Check if double rotation is necessary
                if self.getBalance(node.right) < 0: 
                    node.right = self.rotation(node.right, 'left', 'right')

                # Rotate left
                return self.rotation(node, 'right', 'left')
            elif bal <= -2: 

                # Check if double rotation is necessary
                if self.getBalance(node.left) > 0: 
                    node.left = self.rotation(node.left, 'right', 'left')

                # Rotate right
                return self.rotation(node, 'left', 'right')
            
            return node
        return node

    # Combined left and right together with reference to: https://stackoverflow.com/questions/46858184/how-to-pass-setter-property-as-argument-to-a-function
    def rotation(self, node, dir1, dir2):
        new = node
        node = node.__dict__[dir1]
        old = node.__dict__[dir2]
        node.__dict__[dir2] = new
        new.__dict__[dir1] = old
        return node

    def addHelper(self, node, val):

        # If the next node is none, set it to equal the value
        if val.value > node.value and node.right is None:
            node.right = val
        elif val.value < node.value and node.left is None:
            node.left = val

        # If the value is greater than the current node move right
        elif val.value > node.value:
            node.right = self.addHelper(node.right, val)

        # Otherwise the value is less than the current node and move left
        else: 
            node.left = self.addHelper(node.left, val)

        # Check balance while rolling out of recursion
        return self.balance(node)

    def add(self, value, name, cost):
        # self.addName(value, name, cost)

        val = Node(value, name, cost)

        if self.root is None: self.root = val
        else: self.root = self.addHelper(self.root, val)

        return self

    def findMax(self, node):

        # Recursively finds the largest value from the given root
        if node.right is not None:
            return self.findMax(node.right)
        return node

    def cardHelper(self, node, value):

        # Stop when finding a matching value and return true
        if value == node.value: 
            return node

        if value < node.value and node.left is not None:
           return self.cardHelper(node.left, value)

        if value > node.value and node.right is not None:
           return self.cardHelper(node.right, value)

        return 

    def getCard(self, value):
        if self.root is None: return 'Error' 
        return self.cardHelper(self.root, value)

    def sizeHelper(self, node):
        if node is not None:

            # Recursively adds one for each node that is not none
            return 1 + self.sizeHelper(node.left) + self.sizeHelper(node.right)
        return 0

    def size(self):
        return self.sizeHelper(self.root)

    def preOrder(self, node):
        if node is not None:

            # Recursively appends each node value to a list; starts with the root, traverses the left tree, then the right tree
            return [node.value] + self.preOrder(node.left) + self.preOrder(node.right)
        return []

    def asList(self):
        return self.preOrder(self.root)

    def heightHelper(self, node):
        if node is not None:

            # Recursivley adds one for each node that is not none and returns the max depth of the left and right
            return max(self.heightHelper(node.left), self.heightHelper(node.right)) + 1
        return 0

    def height(self):
        if self.root is None: return 0
        return self.heightHelper(self.root)

    def addNameHelper(self, node, val):
        # If the next node is none, set it to equal the value
        if val.name > node.name and node.rightName is None:
            node.rightName = val
        elif val.name < node.name and node.leftName is None:
            node.leftName = val

        # If the value is greater than the current node move right
        elif val.name > node.name:
            node.rightName = self.addNameHelper(node.rightName, val)

        # Otherwise the value is less than the current node and move left
        else: 
            node.leftName = self.addNameHelper(node.leftName, val)

        # Check balance while rolling out of recursion
        return self.balance(node)

    def addName(self, value, name, cost):
        val = Node(value, name, cost)

        if self.rootName is None: self.rootName = val
        else: self.rootName = self.addNameHelper(self.rootName, val)

        return self

    def cardNameHelper(self, node, value):

        # Stop when finding a matching value and return true
        if value == node.name: 
            return node

        if value < node.name and node.leftName is not None:
            return self.cardNameHelper(node.leftName, value)

        if value > node.name and node.rightName is not None:
            return self.cardNameHelper(node.rightName, value)

        return 

    def getCardName(self, value):
        if self.rootName is None: return 'Error' 
        return self.cardNameHelper(self.rootName, value)

    def preOrderName(self, node):
        if node is not None:

            # Recursively appends each node value to a list; starts with the root, traverses the left tree, then the right tree
            return [node.name] + self.preOrderName(node.leftName) + self.preOrderName(node.rightName)
        return []

    def asListName(self):
        return self.preOrderName(self.rootName)
