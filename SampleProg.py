class Base(object):
    def __init__(self):
        print "Base const"
        self.name = "Base"

    def callBase(self):
        print "base called"

    def test1(self):
        print("Base test1")

class Base1(object):
    def __init__(self):
        print "Base1 const"
        self.name = "Base1"

    def callBase(self):
        print "base1 called"

    def test(self):
        print("Base1 test")


class Children(Base, Base1):
    def __init__(self):
        super(Children, self).__init__()
        print "Child Const"
        self.name = "Child"

    def test(self):
        super(Children, self).test()
        #Base.callBase(self)

    def test1(self):
        super(Children, self).test1()


def run_prog():
    c1 = Children()
    c1.test()
    c1.test1()
    pass

if __name__ == "__main__":
    run_prog()