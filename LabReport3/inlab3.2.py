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

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total = total + 1
            cur = cur.next
        return total

    def traverse(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def erase(self, index):
        if index >= self.length():
            print("ERROR: Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index = cur_index + 1

#creating instance
my_list = linked_list()

print("")
my_list.append("10")
my_list.append("30")
my_list.append("50")
my_list.append("70")
my_list.traverse()
print("")

my_list.erase(2)
my_list.traverse()

print("")
