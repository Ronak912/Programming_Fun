def incr(maxlimit):
    i = 0
    while i < maxlimit:
        yield i * i
        i += 1

func = incr(9)
for i in func:
    print i

# this won't get called
for i in func:
    print i

# this will get called
for i in incr(9):
    print i
