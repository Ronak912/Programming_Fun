# http://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
# ToDo: In above link question is different than the solutions
# A O(n^2) time and O(1) space program to find the
#longest palindromic substring


import sys

# This function prints the longest palindrome substring (LPS)
# of str[]. It also returns the length of the longest palindrome
def longestPalSubstr(string):
    maxLength = 1

    start = 0
    length = len(string)

    low = 0
    high = 0

    # One by one consider every character as center point of
    # even and odd length palindromes
    for i in xrange(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            # if there are equal then compare one left and one right characters and keep
            # incr/decr counter until you can not find matching charcater and save starting
            # point and length of currently found palindromic string

            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    print "Start: ", start
    print "Max Length: ", maxLength
    print "Longest palindrome substring is:",
    print string[start:start + maxLength]

    return maxLength

# A utility function to print a
# substring str[low..high]
def printSubStr(st,low,high) :
    sys.stdout.write(st[low : high + 1])
    sys.stdout.flush()
    return ''

# This function prints the longest palindrome
# substring of st[]. It also returns the length
# of the longest palindrome
def longestPalSubstrDynamicProg(st) :
    n = len(st) # get length of input string

    # table[i][j] will be false if substring
    # str[i..j] is not palindrome. Else
    # table[i][j] will be true
    table = [[0 for x in range(n)] for y
                          in range(n)]

    # All substrings of length 1 are
    # palindromes
    maxLength = 1
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1

    # check for sub-string of length 2.
    start = 0
    i = 0
    while i < n - 1 :
        if (st[i] == st[i + 1]) :
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1

    # Check for lengths greater than 2.
    # k is length of substring
    k = 3
    while k <= n :
        # Fix the starting index
        i = 0
        while i < (n - k + 1) :

            # Get the ending index of
            # substring from starting
            # index i and length k
            j = i + k - 1

            # checking for sub-string from
            # ith index to jth index iff
            # st[i+1] to st[(j-1)] is a
            # palindrome
            if (table[i + 1][j - 1] and
                      st[i] == st[j]) :
                table[i][j] = True

                if (k > maxLength) :
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1

    for i in range(n):
        for j in range(n):
            print table[i][j],
        print("\n")
    print "Longest palindrome substring using dynamic programming is: ",printSubStr(st, start,
                                               start + maxLength - 1)

    return maxLength # return length of LPS


#Driver program to test above functions
string = "forgeeksskeegfor"
print "Length is: " + str(longestPalSubstr(string))

print(longestPalSubstrDynamicProg(string))

#print(longestPalSubstrDynamicProg("abcba"))
