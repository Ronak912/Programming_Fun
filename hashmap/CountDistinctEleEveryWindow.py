# http://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/
#
# Count distinct elements in every window of size k
# Given an array of size n and an integer k, return the of count of distinct numbers in all windows of size k.
#
# Example:
#
# Input:  arr[] = {1, 2, 1, 3, 4, 2, 3};
#             k = 4
# Output:
# 3
# 4
# 4
# 3
#
# Explanation:
# First window is {1, 2, 1, 3}, count of distinct numbers is 3
# Second window is {2, 1, 3, 4} count of distinct numbers is 4
# Third window is {1, 3, 4, 2} count of distinct numbers is 4
# Fourth window is {3, 4, 2, 3} count of distinct numbers is 3


def countDistinctElement(inlst, k):
    hashmap = {}
    distinctcount = 0
    for i in xrange(k):
        val = inlst[i]
        if val not in hashmap:
            hashmap[val] = 1
            distinctcount += 1
        else:
            tmpcnt = hashmap.get(val, 0)
            hashmap[val] = tmpcnt+1

    print distinctcount

    for i in xrange(k, len(inlst)):
        #print inlst[i]
        prevval = inlst[i-k]
        # print "prev:", hashmap[prevval]
        if hashmap[prevval] == 1:
            distinctcount -= 1
            del hashmap[prevval]
        else:
            tmpcount = hashmap[prevval]
            hashmap[prevval] = tmpcount-1

        currval = inlst[i]
        if currval not in hashmap:
            distinctcount += 1
            hashmap[currval] = 1
        else:
            tmpcnt = hashmap[currval]+1
            hashmap[currval] = tmpcnt
        print distinctcount


if __name__ == "__main__":
    lst = [1, 2, 1, 3, 4, 3, 3]
    countDistinctElement(lst, 4)