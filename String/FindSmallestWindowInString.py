# https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

'''Given two strings string1 and string2, find the smallest substring in string1 containing all characters of string2 efficiently.
For Example:

Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
Explanation: "t stri" contains all the characters
              of pattern.

Input :  string = "geeksforgeeks"
         pattern = "ork"
Output :  Minimum window is "ksfor"
'''

import itertools
import collections
import sys


def findSmallestWindow(str1, pat):
    len1 = len(str1)
    patlen = len(pat)

    if len1 < patlen:
        return ''

    patdict = {}

    for char in pat:
        patdict[char] = patdict.get(char, 0) + 1

    min_window, start, start_idx, count = sys.maxint, 0, -1, 0

    str1dict = {}

    for i in range(len(str1)):
        char = str1[i]
        str1dict[char] = str1dict.get(char, 0) + 1
        if patdict.get(char, 0) != 0 and str1dict[char] <= patdict[char]:
            count += 1

        if count == patlen:
            while str1dict[str1[start]] > patdict.get(str1[start], 0) or patdict.get(str1[start], 0) == 0:
                str1dict[str1[start]] -= 1
                start += 1

            windowlen = i-start+1
            if windowlen < min_window:
                min_window = windowlen
                start_idx = start

    if start_idx == -1:
        return ''
    else:
        return str1[start_idx: start_idx+min_window]



if __name__ == "__main__":
    str1 = "this is a test string"
    pat = "tist"
    res = findSmallestWindow(str1, pat)
    print("String with smallest window is: ", res)
