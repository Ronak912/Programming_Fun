

#assume here we have either number or alphabets but there no special character
def sortSubString(inputstr):
    resultstr = ''
    prevtype, tmpstr = '', ''
    for idx, charornum in enumerate(inputstr):
        try:
            tmp = int(charornum)
            currtype = 'inttype'
        except Exception, ex:
            currtype = 'strtype'
        print charornum, "===", currtype

        if (idx > 0 and currtype == prevtype and idx < len(inputstr)-1) or idx == 0:
            tmpstr += str(charornum)
        elif idx == len(inputstr)-1:
            if currtype != prevtype:
                resultstr += ''.join(sorted(tmpstr))
                resultstr += charornum
            else:
                tmpstr += charornum
                resultstr += ''.join(sorted(tmpstr))
        else:
            resultstr += ''.join(sorted(tmpstr))
            tmpstr = charornum
        prevtype = currtype
    return resultstr

if __name__ == '__main__':
    print sortSubString("AZQF013452BAB9876onm")