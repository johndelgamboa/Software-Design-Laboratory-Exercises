class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data, None)
        else:
            self.head = Node(data, None)

    def printList(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
        else:
            print("List is empty")

def concatLL(firstLinkedList, secondLinkedList):
    newList = SLL()
    temp = firstLinkedList.head

    while temp is not None:
        newList.add(temp.data)
        temp = temp.next
    temp = secondLinkedList.head
    while temp is not None:
        newList.add(temp.data)
        temp = temp.next
    return newList

print("First list is -", end=" ")
firstLinkedList = SLL()
firstLinkedList.add(5)
firstLinkedList.add(6)
firstLinkedList.add(7)
firstLinkedList.printList()
print("\nSecond list is -", end=" ")
secondLinkedList = SLL()
secondLinkedList.add(1)
secondLinkedList.add(2)
secondLinkedList.add(3)
secondLinkedList.printList()
print("\nConcatenated list is -", end=" ")
concatenatedList = concatLL(firstLinkedList, secondLinkedList)
concatenatedList.printList()