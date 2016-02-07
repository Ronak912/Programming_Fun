
class Sample:
    def __init__(self):
        self.firstname = 'Ronak'
        self.lastname = 'Agrawal'
        # this is private variable and can not be accessed directly
        self.__private = 'private variable'
        self.private = 'non-private'

    def tuple(self):
        return (self.firstname, self.lastname)

    def getAstuple(self):
        return (self.firstname, self.lastname)

    def getPrivateVar(self):
        return self.__private


if __name__ == '__main__':
    s1 = Sample()
    s2 = Sample()
    Sample.fullname = "XYZ"
    print s1.getPrivateVar()
    print s1.fullname
    print "%s===%s" % (s1.tuple())
    print "NEW"
    s2.firstname = 'binal'
    print s2.fullname
    print s2.firstname, s2.lastname
    try:
        print s2.__private
    except Exception, ex:
        print ex.__str__()
        print "cannot access private variable"