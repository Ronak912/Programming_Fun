# http://www.careercup.com/question?id=16234739

def removeComma(instr):

    inlst = list(instr)
    offset = 0
    for idx in xrange(len(inlst)):
        if inlst[idx] == ',':
            offset += 1
        else:
            inlst[idx-offset] = inlst[idx]

    # this is to remove lst few characters which was already moved to the lower index
    while offset:
        inlst[len(inlst)-offset] = ''
        offset -= 1

    return ''.join(inlst)

if __name__ == '__main__':
    print removeComma('1,234,567,45')