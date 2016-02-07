# http://www.geeksforgeeks.org/longest-consecutive-subsequence/
# Longest Consecutive Subsequence
# Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
#
# Examples
#
# Input: arr[] = {1, 9, 3, 10, 4, 20, 2};
# Output: 4
# The subsequence 1, 3, 4, 2 is the longest subsequence
# of consecutive elements
#
# Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
# Output: 5
# The subsequence 36, 35, 33, 34, 32 is the longest subsequence
# of consecutive elements.

def getMaxLen(inlst):
    hashset = set()
    maxlen = 0

    for val in inlst:
        hashset.add(val)

    for idx, val in enumerate(inlst):
        if val-1 not in hashset:
            # count = 0
            currval = val
            while currval in hashset:
                # count += 1
                currval += 1
            # currval - val: is to get counter. subtrack starting value to get to get count values
            maxlen = max(maxlen, currval-val)

    return maxlen


if __name__ == '__main__':
    print getMaxLen([1, 9, 3, 10, 4, 20, 2, 40, 5, 60, 0, -1])