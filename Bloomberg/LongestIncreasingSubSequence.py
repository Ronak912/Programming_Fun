def findLongestIncreasingSubSequence(inlst):
    subarrlen = 1
    maxsubarraylen = -1
    min_idx, max_idx = 0, 0
    startidx = 0

    for idx in xrange(1, len(inlst)):
        currval = inlst[idx]
        #print idx, currval
        if currval > inlst[idx-1]:
            subarrlen += 1
            # This is to handle max sub array at the end of the original array
            if idx == len(inlst)-1 and subarrlen > maxsubarraylen:
                min_idx, max_idx = startidx, idx
                maxsubarraylen = subarrlen
            #print "Adding Length: ", subarrlen
        elif subarrlen > maxsubarraylen:
            maxsubarraylen = subarrlen
            min_idx = startidx
            max_idx = idx-1
            startidx= idx
            subarrlen = 1
            #print "new array: ", maxsubarraylen, min_idx, max_idx
        else:
            startidx, subarrlen = idx, 1

    return min_idx, max_idx, maxsubarraylen


if __name__ == "__main__":
    print findLongestIncreasingSubSequence([20, 21, 22, 19, 18, 11, 12, 13, 14, 15, 5, 4, 6, 2, 3, 4, 5, 6, 7, 8])