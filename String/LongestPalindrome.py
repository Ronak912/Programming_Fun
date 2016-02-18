# http://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
# ToDo: In above link question is different than the solutions
# A O(n^2) time and O(1) space program to find the
#longest palindromic substring

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

# Driver program to test above functions
string = "forgeeksskeegfor"
print "Length is: " + str(longestPalSubstr(string))
