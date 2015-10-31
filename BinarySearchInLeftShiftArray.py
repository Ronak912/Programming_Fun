"""
Search number in sorted array which is shifted left by unknownnumber
ex: arr = [4,5,6,7,1,2,3], and search for 7 in this array
"""

def binarySearch(lst, searchvalue):
    rotation = 0
    for idx in xrange(len(lst)-1):
        if lst[idx] > lst[idx+1]:
            break
        rotation += 1

    # need to increment by one if array is shifted otherwise it's regular sorted array and nothing should be done
    rotation += 1 if rotation else 0

    start = rotation
    end = len(lst) - 1 + rotation
    position = -1
    print "Start: ", start, "   ", end
    while start <= end:
        mididx = getMid(start, end)
        midvalue = getValAt(lst, mididx)
        print '-------'
        print "mididx: ", mididx, "==", midvalue
        if midvalue == searchvalue:
            position = mididx
            break
        elif midvalue > searchvalue:
            end = mididx - 1
        else:
            start = mididx + 1

    return position % len(lst)

def getValAt(lst, position):
    return lst[position % len(lst)]


def getMid(start, end):
    mid = (start + end) / 2 if (start + end) % 2 == 0 else (start + end + 1) / 2
    return mid



print binarySearch([4,5,6,7,1,2,3], 7)

