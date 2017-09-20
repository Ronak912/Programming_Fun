# http://www.geeksforgeeks.org/find-four-elements-a-b-c-and-d-in-an-array-such-that-ab-cd/

# Find four elements a, b, c and d in an array such that a+b = c+d
# Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct elements. If there are multiple answers, then print any of them.
#
# Example:
#
# Input:   {3, 4, 7, 1, 2, 9, 8}
# Output:  (3, 8) and (4, 7)
# Explanation: 3+8 = 4+7
#
# Input:   {3, 4, 7, 1, 12, 9};
# Output:  (4, 12) and (7, 9)
# Explanation: 4+12 = 7+9
#
# Input:  {65, 30, 7, 90, 1, 9, 8};
# Output:  No pairs found

def findPairs(inlst):
    resdict = {}

    for idx, outerval in enumerate(inlst):
        for innerval in inlst[idx+1:]:
            sum = outerval + innerval
            if sum not in resdict:
                resdict[sum] = [(outerval, innerval)]
            else:
                resdict[sum].append((outerval, innerval))

    for key, val in sorted(resdict.items()):
        # delete values which does not make pairs
        if len(val) % 2 != 0:
            del resdict[key]
    print resdict


if __name__ == "__main__":
    lst = [5, 4, 6, 3, 10, 8]
    findPairs(lst)