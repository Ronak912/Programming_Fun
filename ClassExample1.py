class Spam():

    counter = 0

    @staticmethod
    def count():
        Spam.counter += 1

    def __init__(self):
        self.count()

class Sub(Spam):
    pass
    #counter = 0

class Other(Spam):
    counter = 0


s = Spam()
y1, y2 = Sub(), Sub()

print s.counter, y1.counter, y2.counter