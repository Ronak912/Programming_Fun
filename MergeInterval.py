# Given a collection of pair representing intervals write a function which inserts new interval
# into collection and merges overlapping intervals.
# Example: [-10, -1], [0,2], [4,10] insert [-5, 1] output: [-10, 2], [4, 10]


def mergeInterval11(origlist, newinterval):
    newlst = []
    while origlist:
        oldinterval = origlist.pop(0)
        if newinterval[0] < oldinterval[0]:
            if newinterval[1] < oldinterval[0]:
                newlst += [newinterval, oldinterval] + origlist
            elif newinterval[1] < oldinterval[1]:
                newlst.append((newinterval[0], oldinterval[1]))
                newlst += origlist
            else:
                newlst.append(newinterval)
                newlst += origlist
            origlist = []
        elif newinterval[0] < oldinterval[1]:
            if newinterval[1] < oldinterval[1]:
                newlst.append(oldinterval)
            else:
                newinterval[0] = oldinterval[0]
                newlst.append(newinterval)
            newlst += origlist
            origlist = []
        else:
            newlst.append(oldinterval)
            if not origlist:
                newlst.append(newinterval)
    print "Final List: ", newlst


def mergeInterval(data):
    data = sorted(data)
    print "sorted Data: ", data
    stored = list(data[0])
    newlst = []
    for start, end in data:
        if start < stored[1]:
            stored[1] = max(stored[1], end)
        else:
            newlst.append(tuple(stored))
            stored = [start, end]
    newlst.append(tuple(stored))
    return newlst


if __name__ == '__main__':
    origlist = [(4,9), (20, 22), (1, 3), (24, 32), (23, 31), (12, 15), (8,13), (-10, -5), (-15, -1)]
    print mergeInterval(origlist)