# http://www.careercup.com/question?id=5687263784599552

# Given a sorted array of integers, using the same array, shuffle the integers to have unique elements and return the index.
#
# Sample input : [3, 3, 4, 5, 5, 6, 7, 7, 7]
# Sample output : [3, 4, 5, 6, 7, X, X, X, X]
# In this case, it returns an index of 4.
# The elements in the array after that index is negligible (don't care what value it is).


def swap(lst, first, second):
    temp = lst[first]
    lst[first] = lst[second]
    lst[second] = temp

# This is not efficient soln as we reshuffle list a lot but works very well when array is not sorted
def getUniqueNumAndIndex(inlst):
    hashmap = {}
    # print inlst
    # print inlst[2]

    for idx in range(len(inlst)):
        #print idx, type(idx)
        currval = inlst[idx]
        if currval not in hashmap:
            hashmap[currval] = True
        else:
            inlst.append(inlst.pop(idx))
        # elif idx < len(inlst)-1:
        #     swap(inlst, idx, idx+1)
        #     hashmap[inlst[idx+1]] = True
        #     #print currval, "==", lst
    return inlst

def GetUniqueFromSorted(inlst):
    idx = 1
    if len(inlst) == 0:
        return -1
    elif len(inlst) == 1:
        return 0

    for i in xrange(0, len(inlst)-1):
        if inlst[i] < inlst[i+1]:
            inlst[idx] = inlst[i+1]
            idx += 1

    print inlst
    return idx-1


if __name__  ==  "__main__":
    #print getUniqueNumAndIndex([3, 3, 4, 5, 5, 6, 8, 8, 7, 7, 7])
    print GetUniqueFromSorted([3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8])