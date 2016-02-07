# http://www.geeksforgeeks.org/given-an-array-of-pairs-find-all-symmetric-pairs-in-it/

# Given an array of pairs, find all symmetric pairs in it
# Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d. For example (10, 20) and (20, 10) are symmetric. Given an array of pairs find all symmetric pairs in it.
#
# It may be assumed that first elements of all pairs are distinct.
#
# Example:
#
# Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
# Output: Following pairs have symmetric pairs
#         (5, 10) and (10, 5)


def findPairs(inlst):
    resdict = {}

    for first, sec in inlst:
        if resdict.get(sec, False) == first:
            print "({}, {}) and ({}, {})".format(first, sec, sec, first)
        else:
            resdict[first] = sec

if __name__ == '__main__':
    lst = [(10,20), (30, 40), (50,60), (20,10), (90,80), (40, 30)]
    findPairs(lst)
