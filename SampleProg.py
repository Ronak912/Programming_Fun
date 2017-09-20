class Base(object):
    def __int__(self):
        print "Base const"
        self.name = "Base"

    def callBase(self):
        print "base called"

class Children(Base):
    def __int__(self):
        print "Child Const"
        self.name = "Child"

    def test(self):
        Base.callBase(self)


def run_prog():
    c1 = Children()
    c1.test()
    pass

if __name__ == "__main__":
    run_prog()