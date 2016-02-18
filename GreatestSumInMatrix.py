
arr = [[4, 7, 1], [6, 9, 1], [50, 10, 45]]

def numberOfPaths(m, n):
    # If either given row number is first or given column number is first
    if m == 1 or n == 1:
        return 1

    # If diagonal movements are allowed then the last addition is required.
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) # +  numberOfPaths(m-1,n-1)


def numberOfPathsUsingDP(m, n):

    # Create a 2D table to store results of subproblems
    # lstdp = []
    # for i in xrange(m):
    #     lstdp.append([0 for j in xrange(n)])
    # print lstdp

    lstdp = [[0 for j in xrange(n)] for i in xrange(m)]

    # Count of paths to reach any cell in first column is 1
    for i in xrange(m):
        lstdp[i][0] = 1

    # Count of paths to reach any cell in first column is 1
    for j in xrange(n):
        lstdp[0][j] = 1

    # Calculate count of paths for other cells in bottom-up manner using
    # the recursive solution
    for i in xrange(1, m):
        for j in xrange(1, n):
            # By uncommenting the last part the code calculatest he total
            # possible paths if the diagonal Movements are allowed
             lstdp[i][j] = lstdp[i-1][j] + lstdp[i][j-1]   # + count[i-1][j-1];

    print lstdp
    return lstdp[m-1][n-1]


def maxValue():
    r = 3
    c = 3
    maxValues = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                maxValues[i][j] = arr[i][j]
            elif i == 0:
                maxValues[i][j] = maxValues[i][j-1] + arr[i][j]
            elif j == 0:
                maxValues[i][j] = maxValues[i-1][j] + arr[i][j]
            else:
                maxValues[i][j] = max(maxValues[i][j-1], maxValues[i-1][j]) + arr[i][j]
    return maxValues[r-1][c-1]


if __name__ == '__main__':
    #print "Total: ", numberOfPaths(3,3)
    print "Total: ", maxValue()
    print "Total Possible Paths: ", numberOfPaths(3, 3)
    print "possible paths: ", numberOfPathsUsingDP(3, 3)