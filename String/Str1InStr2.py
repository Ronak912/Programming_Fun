# Recursive Python program to check if a string is subsequence
# of another string

# Returns true if str1[] is a subsequence of str2[]. m is
# length of str1 and n is length of str2
def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False

    # If last characters of two strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)

    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)

def isSubSequenceIter(string1, string2, m, n):
    i, j = 0, 0
    while j < n:
        if i >= m or j >= n:
            return False
        if string1[i] == string2[j]:
            if i == m-1:
                return True
            i += 1
        j += 1
    return False


# Driver program to test the above function
string1 = "gksrek"
string2 = "geeksforgeeks"
m = len(string1)
n = len(string2)
if isSubSequenceIter(string1, string2, m, n):
    print "Yes"
else:
    print "No"