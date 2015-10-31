def incr(maxlimit):
    i = 0
    while i < maxlimit:
        yield i
        i += 1

for i in incr(9):
    print i
