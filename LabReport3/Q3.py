class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def second_to_last(self):
        cur_node = self.head

        if cur_node.next == None:
            return -1

        while cur_node.next != None:
            if cur_node.next.next == None:
                return cur_node.data

            cur_node = cur_node.next

    def traverse(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


list = linked_list()

print("")
list.append("10")
list.append("5")
list.append("15")
list.append("25")
list.append("20")
list.traverse()
print("")

print(list.second_to_last())
