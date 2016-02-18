

def reverseNumberIter(innum):
    outnumber = 0
    while innum:
        outnumber = (outnumber * 10) + innum % 10
        innum = innum //10

    return outnumber


if __name__ == '__main__':
    #print reverseNumberRecur(12345)
    print reverseNumberIter(12345)