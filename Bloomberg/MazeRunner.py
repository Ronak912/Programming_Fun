# Another way if we want to save path in matrix using 0 and 1
# http://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/

m, n = None, None

count = 0

def isFoundDestination(matrix, _m, _n):
    global m, n
    m = _m
    n = _n
    traverseUtilToCount(matrix, 0, 0)
    return traverseUtil(matrix, 0, 0)


def traverseUtil(matrix, x, y):

    if x == m-1 and y == n-1:
        return True

    if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] == 1:
        return traverseUtil(matrix, x+1, y) or traverseUtil(matrix, x, y+1)

    return False


def traverseUtilToCount(matrix, x, y):
    global count

    if x == m-1 and y == n-1:
        count += 1

    if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] == 1:
        return traverseUtilToCount(matrix, x+1, y) or traverseUtilToCount(matrix, x, y+1)

    return False

if __name__ == "__main__":
    ''' We start from from the top left corner and we want to reach to the bottom right corner
        and we can only traverse through the 1'''
    matrix = [[1, 1, 0],
              [1, 1, 0],
              [0, 1, 1]
             ]
    print isFoundDestination(matrix, 3, 3)
    print "Total Path: ", count