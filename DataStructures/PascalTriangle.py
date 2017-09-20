# http://www.geeksforgeeks.org/pascal-triangle/

# ToDo: can be done using few different approach but this one is more efficient,
# We can also use 2D array which is easy to understand but required O(N^2) extra space

# Formula to calculate number based on line and ith position
# C(line, i)   = line! / ( (line-i)! * i! )
# C(line, i-1) = line! / ( (line - i + 1)! * (i-1)! )
# We can derive following expression from above two expressions.
# C(line, i) = C(line, i-1) * (line - i + 1) / i
#
# So C(line, i) can be calculated from C(line, i-1) in O(1) time

def printPascal(n):
    print "======Using previous value=========="
    for line in xrange(1, n+1):
        C = 1  # used to represent C(line, i)
        for i in xrange(1, line+1):
            print C, " ",  # The first value in a line is always 1
            C = C * (line - i) / i
        print ''
    print "=================="

def getPascalTriangleUsingArray(n):
    pastriangle = []
    for line in xrange(0, n):
        tmpline = []
        for k in xrange(0, line+1):
            # print line, "==", k
            if k == 0 or k == line:
                currval = 1
            else:
                # print pastriangle[line-1][k-1],  pastriangle[line-1][k]
                currval = pastriangle[line-1][k-1] + pastriangle[line-1][k]
            tmpline.append(currval)
        pastriangle.append(tmpline)

    print "=====Using 2D array==="
    for line in pastriangle:
        for val in line:
            print val, " ",
        print ""
    print "=================="


# http://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
def GetOneNumber(line, element_idx):
    result = 1

    if element_idx > line-element_idx:
        k = line - element_idx
    else:
        k = element_idx

    for i in xrange(0, k):
        result *= (line-i)
        result /= (i+1)
    return result

if __name__ == "__main__":
    printPascal(5)
    getPascalTriangleUsingArray(10)
    print "Number: ", GetOneNumber(4, 2), "  ", GetOneNumber(4, 3)