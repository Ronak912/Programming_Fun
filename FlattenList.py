A = [2, 3, [1, 2], [5, [6, [3]], 7], 2]
#sorted(flatten(A)) == sorted([2, 3, 1, 2, 5, 6, 3, 7, 2])


def FlattenListUsingIter1(temp):
    tmplst = []
    for value in temp:
        if not isinstance(value, list):
            tmplst.append(value)
        else:
            newtmplst = value
            for innerval in newtmplst:
                if not isinstance(innerval, list):
                    tmplst.append(innerval)
                else:
                    newtmplst.extend(innerval)
    print tmplst

#print "Flatten List Using Iteraton: ", FlattenListUsingIter1(A)

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

def FlattenListUsingIter11(inlst):
    tmplst = []
    for currval in inlst:
        #temp = temp[1:]  # if len(temp) > 1 else [temp[0]] if temp else []
        if isinstance(currval, list):
            for innerval in currval:
                if isinstance(innerval, list):
                    inlst.extend(innerval)
                else:
                    tmplst.append(innerval)
        else:
            tmplst.append(currval)
    return tmplst



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



def getFlattenList11(inlst):
    newlst = []
    exposedlst = []
    for val in inlst:
        if isinstance(val, int):
            newlst.append(val)
        elif isinstance(val, list):
            exposedlst.extend(val)
    while exposedlst:
        currval = exposedlst.pop()
        if isinstance(currval, list):
            exposedlst.extend(currval)
        else:
            newlst.append(currval)
    print "List: ", newlst



#print "Flatten List Using Iteraton: ", getFlattenList11(A)
print "Flatten List Using Iteraton: ", FlattenListUsingIter11(A)
#print "Flatten List Using Recursion:", getFlattenList(A)