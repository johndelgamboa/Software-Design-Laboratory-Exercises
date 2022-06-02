class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) < 1:
            return None
        return self.items.pop()


    def peek(self):
        if len(self.items) < 1:
            return None
        return self.items[-1]

    def len(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "_main_":
    s = Stack()
    print()
    print("Check if the list is empty")
    print(s.is_empty())
    print("")
    print("inserting 300, 100, and 200")
    s.push("300")
    s.push("100")
    s.push("200")
    print(s)
    print("")

    print("popping :", s.pop())
    print("popping :", s.pop())
    print(s)
    print()
    print("peek the latest element:",s.peek())
    print("")
    print("push 500 to the list")

    s.push("500")
    print(s)
    print("")

    print("length of the list: ",s.len())
    print("")
