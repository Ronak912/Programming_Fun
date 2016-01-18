# Given a collection of pair representing intervals write a function which inserts new interval
# into collection and merges overlapping intervals.
# Example: [-10, -1], [0,2], [4,10] insert [-5, 1] output: [-10, 2], [4, 10]


def mergeInterval(origlist, newinterval):
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


if __name__ == '__main__':
    origlist = [[-10, -1],[0, 2],[4, 10]]
    mergeInterval(origlist, [1, 5])