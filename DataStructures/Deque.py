class Deque(object):
    def __init__(self, size = 100):
        self.items = []
        self.__currsize = 0
        self.size = size

    def addFront(self, item):
        if self.__currsize >= self.size:
            return False
        self.__currsize += 1
        self.items.append(item)

    def removeFront(self):
        if self.__currsize <=0:
            return False
        self.__currsize -= 1
        return self.items.pop()

    def addRear(self, item):
        if self.__currsize >= self.size:
            return False
        self.__currsize += 1
        self.items.insert(0, item)

    def removeRear(self):
        if self.__currsize <= 0:
            return False
        self.__currsize -= 1
        return self.items.pop(0)

    def isEmpty(self):
        return self.__currsize == 0

    def getSize(self):
        return self.__currsize

    def __str__(self):
        return ' '.join([str(val) for val in self.items])


if __name__ == '__main__':
    deque = Deque()
    deque.addFront(1)
    deque.addFront(2)
    deque.addFront(3)
    deque.removeFront()
    deque.addRear(11)
    deque.addRear(12)
    deque.addRear(13)
    deque.removeRear()
    print deque

