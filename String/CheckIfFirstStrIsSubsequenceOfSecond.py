# http://www.geeksforgeeks.org/given-two-strings-find-first-string-subsequence-second/

# Given two strings, find if first string is a subsequence of second
# Given two strings str1 and str2, find if str1 is a subsequence of str2. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements (source: wiki). Expected time complexity is linear.
#
# Examples:
#
# Input: str1 = "AXY", str2 = "ADXCPY"
# Output: True (str1 is a subsequence of str2)
#
# Input: str1 = "AXY", str2 = "YADXCP"
# Output: False (str1 is not a subsequence of str2)
#
# Input: str1 = "gksrek", str2 = "geeksforgeeks"
# Output: True (str1 is a subsequence of str2)

def isSubString(str1, str2):
    m = len(str1)
    n = len(str2)
    if m == 0:
        return True

    if n == 0 or n < m:
        return False

    i, j = 0, 0

    while i < m and j < n:
        if str1[i] == str2[j]:
            i += 1
        j += 1

    #print "m: ", m, "i=", i
    return True if i >= m else False


if __name__ == '__main__':
    str1 = "ronak"
    str2 = "raognraawakl"
    print isSubString(str1, str2)
    # Should return False
    print isSubString("ronakg", str2)