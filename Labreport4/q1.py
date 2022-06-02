from imp import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def insertInList(self, key):
        temp = Node(key)
        temp.setNext(self.head)
        self.head = temp

    def displayList(self):
        temp = self.head
        while temp != None:
            print(temp.getData(), end=" ")
            temp = temp.getNext()
        print()

    def searchReference(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                return current
            else:
                current = current.getNext()
        return None

    def swap2Nodes(self, n1, n2):
        prev1 = None
        prev2 = None
        next1 = None
        next2 = None
        curr = self.head

        while curr != None:
            if curr == n1:
                break
            prev1 = curr
            curr = curr.getNext()

        next1 = curr.getNext()

        curr = self.head
        while curr != None:
            if curr == n2:
                break
            prev2 = curr
            curr = curr.getNext()
        next2 = curr.getNext()

        prev1.setNext(n2)
        n2.setNext(next1)

        prev2.setNext(n1)
        n1.setNext(next2)


def main():
    list1 = LinkedList()
    list1.insertInList(10)
    list1.insertInList(40)
    list1.insertInList(13)
    list1.insertInList(56)
    list1.insertInList(78)
    list1.insertInList(11)
    list1.insertInList(9)
    list1.insertInList(38)

    print("Initial list: ")
    list1.displayList()

    n11 = list1.searchReference(11)
    n13 = list1.searchReference(13)

    if n11 != None and n13 != None:
        list1.swap2Nodes(n11, n13)
    else:
        print("Nodes not found")

    print("after swapping 11 and 13")
    list1.displayList()


if __name__ == "__main__":
    main()