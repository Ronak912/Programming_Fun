# http://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-delete-search-and-getrandom-in-constant-time/

# Design a data structure that supports insert, delete, search and getRandom in constant time
# Design a data structure that supports following operations in Θ(1) time.
#
# insert(x): Inserts an item x to the data structure if not already present.
#
# remove(x): Removes an item x from the data structure if present.
#
# search(x): Searches an item x in the data structure.
#
# getRandom(): Returns a random element from current set of elements

import random

class HashMapArray(object):
    def __init__(self):
        self.__hashmap = {}
        self.__mylist = []

    def add(self, value):
        if self.__hashmap.get(value, None):
            return False

        size = len(self.__mylist)
        self.__hashmap[value] = size
        self.__mylist.append(value)

        return True

    def delete(self, value):
        if value not in self.__hashmap:
            return False

        size = len(self.__mylist)
        lastvalue = self.__mylist[size - 1]
        valueidx = self.__hashmap.get(value, 0)

        # delete entry from hashmap and update index of last array element
        del self.__hashmap[value]
        self.__hashmap[lastvalue] = valueidx

        # reposition last element to deleted value index
        # purpose of doing this is to avoid shifting all the values to previous position which is O(n)
        self.__mylist[valueidx] = lastvalue
        del self.__mylist[size-1]

        return True


    def search(self, value):
        if value not in self.__hashmap:
            return False

        return self.__hashmap.get(value, 0)


    def getRandom(self):
        randidx = random.randint(0, len(self.__mylist)-1)
        return self.__mylist[randidx]

    def getArray(self):
        return self.__mylist

    def getHashMap(self):
        return self.__hashmap


if __name__ == '__main__':
    clsobj = HashMapArray()
    clsobj.add(1)
    clsobj.add(2)
    clsobj.add(3)
    clsobj.add(4)
    clsobj.add(5)
    clsobj.add(6)
    clsobj.add(7)

    print "Search for 4: ", clsobj.search(4)

    print "Delete number 6: ", clsobj.delete(3)

    print "Search for deleted number 6: ", clsobj.search(3)

    print "Insert number 8: ", clsobj.add(8)

    print "Get Random number from Class: ", clsobj.getRandom()

    print "Array: ", clsobj.getArray()

    print "HashMap: ", clsobj.getHashMap()
