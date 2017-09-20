class Stack(object):
    def __init__(self):
        self.lst = []
        self.size = 0

    def push(self, value):
        self.size += 1
        self.lst.append(value)

    def pop(self):
        self.size -= 1
        return self.lst.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.lst[self.size - 1]  #or self.lst[-1]


    def peekbyidx(self, idx):
        if idx > self.size - 1 or idx < 0:
            raise Exception("out of range")
        return self.lst[self.size-1-idx]

    def getsize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


    def __str__(self):
        return ", ".join([str(val) for val in self.lst])


if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print "pop: ", stack.pop()
    print "peek: ", stack.peek()
    print "peek by index: ", stack.peekbyidx(0)
    print "Size: ", stack.getsize()
    print "Stack: ", stack
