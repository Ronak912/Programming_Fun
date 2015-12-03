from datetime import datetime

import time

print "Ddate: ", datetime.now()
#print (time.strftime("%H:%M:%S"))

customcache = {}


def decFunc(func):
    global customcache
    def func_wrapper(*args, **kwargs):
        key = args[0]
        if key not in customcache:
            ret = func(*args, **kwargs)
            currdttime = datetime.now()
            customcache[key] = (ret, currdttime)
            return ret
        else:
            print "From Cache"
            currdttime = datetime.now()
            origval, startime = customcache[key]
            totalseconds = (currdttime - startime).seconds
            if totalseconds < 5:
                return origval
            else:
                ret = func(*args, **kwargs)
                customcache[key] = (ret, currdttime)
                return ret

    return func_wrapper


@decFunc
def foo(temp):
    print "Calling Actual Func"
    return (temp ** temp)


foo(5)
time.sleep(7)
foo(5)
print "Cache: ", customcache
