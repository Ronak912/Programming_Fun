def dpLps(a, i, j, lps):

    if i > j:
        return 0

    if lps[i][j] == 0:
        if i == j:
            lps[i][j] = 1
        else:
            if a[i] == a[j]:
                # here a[i] and a[j] is part of palindrome and so value is 2 (as we found 2 values)
                lps[i][j] = 2 + dpLps(a, i + 1, j - 1, lps)
            else:
                lps[i][j] = max(dpLps(a, i + 1, j, lps), dpLps(a, i, j - 1, lps))
	return lps[i][j]


def findLongestPalindrome(a, lps):
    n = len(a)
    for i in xrange(n):
        lps[i][i] = 1

    for cl in xrange(2, n+1):
        for i in xrange(0, n-cl+1):
            j = i + cl - 1
            if a[i] == a[j] and cl == 2:
                lps[i][j] = 2
            elif a[i] == a[j]:
                lps[i][j] = 2 + lps[i+1][j-1]
            else:
                lps[i][j] = max(lps[i+1][j], lps[i][j-1])

    return lps[0][n-1]


if __name__ == '__main__':
    a = [2, 4, 1, 3, 7, 6, 8, 1, 4, 2]
    lps = []

    for i in xrange(len(a)):
        lps.append([0 for j in xrange(len(a))])

    #print "LPS: ", lps
    # This is recursion solution
    #lpsnew = dpLps(a, 0, len(a)-1, lps)
    #print "After: ", lpsnew

    print findLongestPalindrome(a, lps)