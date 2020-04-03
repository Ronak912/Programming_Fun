# Length of longest common subsequence
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# https://www.geeksforgeeks.org/printing-longest-common-subsequence/

def getLongestCommonSubSequence(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n+1) for _ in xrange(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # dp[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    print("Longest length is: ", dp[m][n])
    lcslen = dp[m][n]

    lcs = ["" for _ in range(lcslen)]
    idx = lcslen
    i = m
    j = n
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs[idx-1] = a[i-1]
            i -= 1
            j -= 1
            idx -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("Longest Common SubSequence: ", ''.join(lcs))


def lcsRecur(X, Y, m, n):

    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcsRecur(X, Y, m-1, n-1)
    else:
       return max(lcsRecur(X, Y, m, n-1), lcsRecur(X, Y, m-1, n))

if __name__ == "__main__":
    # Get longest common subsequence
    getLongestCommonSubSequence("ABCDGH", "AEDFHR")
