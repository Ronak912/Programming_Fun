# http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


def findLargestSum(inlst):

    length = len(inlst)
    currmax, max_so_far = inlst[0], inlst[0]
    for i in xrange(1, length):
        currmax = max(inlst[i], currmax+inlst[i])
        max_so_far = max(max_so_far, currmax)

    return max_so_far

if __name__ == "__main__":
    print findLargestSum([-2, -3, 4, -1, -2, 1, 5, -3])



