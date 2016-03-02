
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



class Sample1:
    def __init__(self, lst1, lst2):
        for key, val in zip(lst1, lst2):
            self.__dict__[key] = val

    def __str__(self):
        return dir(self)

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

    #use if dir, dict within class
    s1 = Sample1(['a', 'b', 'c'], ['abc', 'bce', 'cde'])
    print "Structure: ", dir(Sample1)
    print "Class dict: ", s1.__dict__
    print s1.a
    print s1.b
    #print s1