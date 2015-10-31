
class Sample:
    def __init__(self):
        self.firstname = 'Ronak'
        self.lastname = 'Agrawal'

    def tuple(self):
        return (self.firstname, self.lastname)

    def getAstuple(self):
        return (self.firstname, self.lastname)


if __name__ == '__main__':
    s1 = Sample()
    s2 = Sample()
    Sample.fullname = "XYZ"
    print s1.fullname
    print "%s===%s" % (s1.tuple())
    print "NEW"
    s2.firstname = 'binal'
    print s2.fullname
    print s2.firstname, s2.lastname
