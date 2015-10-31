"""
Find three values from given array which can make Triangle
Condition for triangle is:
    A + B > C
    B + c > A
    A + C > B

e.g: 6,4,5 can form triangle but
    4,5,10 can not
"""

# Strategy here is to sort array first and then check for three consequtive number starting from 0th index
# if a < b < c and a + b > c then always a + c > b and b + c > a


def isTriangle(a, b, c):
    if a + b > c:
        return True
    return False

def findTriangle(inputlst):
    if len(inputlst) < 2:
        return 'not enough value to form Triangle'
    inputlst.sort()
    i = 0
    j = 1
    k = 2

    while k < len(inputlst):
        if isTriangle(inputlst[i], inputlst[j], inputlst[k]):
            print inputlst[i], "--", inputlst[j], "--", inputlst[k]
            return True
        i += 1
        j += 1
        k += 1
    return False


# This will return all the possibility
def getAllTriangle(inputlst):
    if len(inputlst) < 2:
        return 'not enough value to form Triangle'
    inputlst.sort()
    i = 0

    trianglelst = []
    while i < len(inputlst) - 2:
        j = i + 1
        while j < len(inputlst) - 1:
            k = j + 1
            while k < len(inputlst):
                if isTriangle(inputlst[i], inputlst[j], inputlst[k]):
                    trianglelst.append((inputlst[i], inputlst[j], inputlst[k]))
                else:
                    # if it's not triangle then there is no meaning of checking next one,
                    # as it's sorted array and next series will not make triangle
                    break
                k += 1
            j += 1
        i += 1
    print "All Triangle: ", trianglelst

findTriangle([4, 5, 12, 13, 15, 20])
getAllTriangle([4, 5, 6, 7, 12, 13, 15, 20])

