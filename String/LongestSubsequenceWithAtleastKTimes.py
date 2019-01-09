# https://www.geeksforgeeks.org/longest-subsequence-where-every-character-appears-at-least-k-times/
'''
Method 1 (Brute force)
We generate all subsequences (check file GetAllSubString.py).
For every subsequence count distinct characters in it and find the longest subsequence where every character
appears at-least k times.

Method 2 (Efficient way)
1. Find the frequency of the string and store it in an integer array of size 26 representing the alphabets.
2. After finding the frequency iterate the string character by character and if the frequency of that character
    is greater than or equal to the required number of repetitions then print that character then and there only.
'''

import collections

def longestSubseqWithK(instr, k):
    map = collections.defaultdict(int)
    for char in instr:
        map[char] += 1

    outputstr = ''
    for char in instr:
        if map[char] >= k:
            outputstr += char

    print(outputstr)


if __name__ == "__main__":
    longestSubseqWithK("ronakronaktest", 2)