# Singleton/ClassVariableSingleton.py
class SingleTone(object):
    __instance = None
    def __new__(cls, val):
        print "inside"
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        SingleTone.__instance.val = val
        return SingleTone.__instance

    def getValue(self):
        return SingleTone.__instance.val


if __name__ == "__main__":
    obj1 = SingleTone(10)
    obj2 = SingleTone(20)
    print obj1.getValue()
    print obj2.getValue()