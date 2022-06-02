class Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def append(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.append(data)
            else:
                self.left = Tree(data)
        else:
            if self.right:
                self.right.append(data)
            else:
                self.right = Tree(data)

    def preOrder(self):
        element = [self.data]

        if self.left:
            element += self.left.preOrder()

        if self.right:
            element += self.right.preOrder()

        return element

    def inOrder(self):
        element = []

        if self.left:
            element += self.left.inOrder()
        element.append(self.data)

        if self.right:
            element += self.right.inOrder()
        return element

    def postOrder(self):
        element = []
        if self.left:
            element += self.left.postOrder()

        if self.right:
            element += self.right.postOrder()

        element.append(self.data)

        return element

    def Count(self):
        element = []

        if self.left:
            element += self.left.inOrder()
        element.append(self.data)

        if self.right:
            element += self.right.inOrder()

        count = len(element)
        return count


def CreateBST(element):
    node = Tree(element[0])

    for i in range(1, len(element)):
        node.append(element[i])

    return node


if __name__ == "__main_":
    num = [50, 35, 23, 41, 100, 75, 87]
    bst = (CreateBST(num))
    print("")

    print("Traversing in Pre-order")
    print(bst.preOrder())
    print("")

    print("Traversing in Post-order")
    print(bst.postOrder())
    print("")

    print("Traversing in In-order")
    print(bst.inOrder())
    print("")

    print(bst.Count())
    print("")