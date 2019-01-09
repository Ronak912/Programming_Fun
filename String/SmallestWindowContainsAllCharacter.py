# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/

'''Smallest window that contains all characters of string itself
Given a string, find the smallest window length with all distinct characters of the given string.
For eg. str = "aabcbcdbca", then the result would be 4 as of the smallest window will be "dbca"
Examples:

Input  : aabcbcdbca
Output : dcba
Explanation :
dbca of length 4 is the smallest
window with highest number of distinct
characters.

Input : aaab
Output : ab
Explanation :
ab of length 2 is the smallest window
with highest number of distinct characters. '''

import sys
from collections import defaultdict


def findSubString(inputstr):
    distinctcounts = len(set(inputstr))

    start, startidx, minwindow, windowlen = 0, -1, sys.maxint, -1

    charcount = defaultdict(lambda: 0)
    count = 0

    for i in range(len(inputstr)):
        char = inputstr[i]
        charcount[char] += 1
        if charcount[char] == 1:
            count += 1

        if count == distinctcounts:
            while charcount[inputstr[start]] > 1:
                if charcount[inputstr[start]] > 1:
                    charcount[inputstr[start]] -= 1
                start += 1

            windowlen = i - start + 1
            if minwindow > windowlen:
                minwindow = windowlen
                startidx = start

    return inputstr[startidx:startidx+minwindow]


if __name__=='__main__':
    print("Smallest window containing all distinct characters is {}"
         .format(findSubString("aabcbcdbca")))
