
def findSecondLargest(inlst):

    print "Sorted List: ", sorted(inlst)

    maxnum, secmax = inlst[0], 0

    for idx in xrange(1, len(inlst)):
        currval = inlst[idx]
        if currval > maxnum:
            secmax = maxnum
            maxnum = currval
        elif currval > secmax:
            secmax = currval
        continue
    return secmax

if __name__ == '__main__':
    print findSecondLargest([100, 101, 22, 33, 88, 44, 55, 99, 66, 77])