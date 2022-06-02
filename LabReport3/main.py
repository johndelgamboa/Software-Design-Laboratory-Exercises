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

    def count_recursive(self, head):
        if not head:
            return 0
        else:
            return 1 + self.count_recursive(head.next)

    def count_recur(self):
        return self.count_recursive(self.head) - 1

    def traverse(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


list = linked_list()

list = linked_list()

print("")
list.append("10")
list.append("5")
list.append("15")
list.append("25")
list.append("20")

list.traverse()
print("")

print(list.count_recur())
