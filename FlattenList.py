A = [2, 3, [1, 2], [5, [6, [3]], 7], 2]
#sorted(flatten(A)) == sorted([2, 3, 1, 2, 5, 6, 3, 7, 2])

def FlattenListUsingIter(temp):
    tmplst = []
    while temp:
        currval = temp[0]
        temp = temp[1:]  # if len(temp) > 1 else [temp[0]] if temp else []
        if isinstance(currval, list):
            for innerval in currval:
                temp.insert(0, innerval)
        else:
            tmplst.append(currval)    
    return tmplst

print "Flatten List Using Iteraton: ", FlattenListUsingIter(A)

# Using Recursion

def getFlattenList(temp):
    tmplst = []
    for val in temp:
        if isinstance(val, list):
            tmplst += getValueFromList([], val)
        else:
            tmplst.append(val)
    return tmplst

def getValueFromList(newlst, currlist):
    for value in currlist:
        if isinstance(value, list):
            getValueFromList(newlst, value)
        else:
            newlst.append(value)
    return newlst


print "Flatten List Using Recursion:", getFlattenList(A)