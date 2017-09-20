class Mapping(dict):
    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        print "Length method: "
        return len(self.__dict__)

mymap = Mapping()
mymap['r'] = 'ronak'
print mymap['r']
print len(mymap)

