class Queue:
    def __init__(self, size):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        self.items.append(item)
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return False
        self.size -= 1
        return self.items.pop(0)

    def getsize(self):
        return self.size

    def __str__(self):
        return ' '.join([str(val) for val in self.items])

if __name__ == "__main__":
    queue = Queue(10)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    queue.dequeue()
    print queue  # or str(queue)