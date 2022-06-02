class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, items):
        return self.items.append(items)

    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop(0)

    def peek(self):
        if len(self.items) < 1:
            return None
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main_":
    q = Queue()
    print("")
    q.enqueue("H")
    q.enqueue("E")
    q.enqueue("L")
    q.enqueue("L")
    q.enqueue("O")
    print(q)

    print("")

    q.dequeue()
    print(q)
    print(q.peek())
    print("")
