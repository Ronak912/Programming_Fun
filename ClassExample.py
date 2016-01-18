class x():
    pass

class y():
    pass

class z():
    def test(self):
        print 'z'

class A(x, y):
    def testA(self):
        print "A"

class B(y, z):
    def testB(self):
        print "B"

class M(B, A, z):
   pass

M.test(M())
