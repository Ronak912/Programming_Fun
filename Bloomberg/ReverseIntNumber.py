import sys

def reverseNumberIter(innum):
    outnumber = 0
    while innum:
        outnumber = (outnumber * 10) + innum % 10
        innum //= 10

    return outnumber


def reverNumberRecur(innum, revnum=0):
    if innum <=0:
        return revnum + innum
    revnum = revnum *10 + innum%10
    return reverNumberRecur(innum//10, revnum)



if __name__ == '__main__':
    #print reverNumberRecur(123405)
    print reverseNumberIter(123405)