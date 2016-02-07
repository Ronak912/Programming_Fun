rowmax = 3
colmax = 3
arr = [[4, 7, 1], [6, 9, 1], [50, 10, 45]]
finalsum = 0

def numberOfPaths(m, n):
   # If either given row number is first or given column number is first
   if m == rowmax and n == colmax:
        finalsum = sum

   # If diagonal movements are allowed then the last addition is required.
   return  numberOfPaths(m-1, n) + numberOfPaths(m, n-1)



def maxValue():
    r = 3
    c = 3
    maxValues = [[0, 0, 0],[0, 0,0],[0, 0, 0]]
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

def run_prog():
    #print "Total: ", numberOfPaths(3,3)
    print "Total: ", maxValue()


def getCell(sum, row, col):
    sum += arr[row][col]
    if row == rowmax -1:
        row = col + 1
    if col == colmax -1:
        col = row + 1
    sum += getCell(sum, row, col)


if __name__ == '__main__':
    run_prog()