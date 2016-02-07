# This is to show how simple iterator can be converted into recursive
# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html

totalcalls = 0

def sumofnumbersIter(inlst):
    totalsum = 0
    for val in inlst:
        totalsum += val
    return totalsum

def sumofnumbersRecur(inlst):
    global totalcalls
    totalcalls += 1
    if len(inlst) == 1:
        return inlst[0]
    else:
        return inlst[0] + sumofnumbersRecur(inlst[1:])

if __name__ == '__main__':
    print sumofnumbersIter([1, 2, 3, 4, 5, 6])
    print sumofnumbersRecur([1, 2, 3, 4, 5, 6])
    print "Total calls: ", totalcalls