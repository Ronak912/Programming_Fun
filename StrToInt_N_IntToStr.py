def strToInt1(inputstr):
    totalchar = len(inputstr)
    if totalchar == 0:
        return 0
    if inputstr[0] == '-':
        isNeg = True
        index = 1
    else:
        index = 0
        isNeg = False

    number = 0
    while index < totalchar:
        number *= 10
        number += int(inputstr[index])
        index += 1

    number *= -1 if isNeg else 1

    print "String To Number is: ", number

def inttoStr(inputnum):
    if inputnum == 0:
        return '0'
    if inputnum < 0:
        isNeg = True
        inputnum *= -1
    else:
        isNeg = False

    tmplst = []
    while inputnum:
        currdigit = inputnum % 10
        inputnum /= 10
        tmplst.append(str(currdigit))

    newstr = '-' if isNeg else ''
    while tmplst:
        newstr += tmplst.pop()
    # index = len(tmplst)
    # while index > 0:
    #     index -= 1
    #     newstr += tmplst[index]

    print "Number To String: ", newstr


if __name__ == '__main__':
    inputstr = '-1305'
    strToInt1(inputstr)
    inttoStr(-1037)