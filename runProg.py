class Top(object):
    def hello(self):
        return "Top"
class MidOne(Top):
    def hello1(self):
        return "MidOne"
class MidTwo(Top):
    def hello(self):
        return "MidTwo"
class Bottom(MidOne, MidTwo):
    pass

print Bottom().hello()
