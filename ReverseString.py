

def reverseString(instr):
    outstr = ''
    for idx in xrange(len(instr)-1, -1, -1):
        outstr += instr[idx]

    print "Reverse String: ", outstr

    mididx = int(len(instr)/2)
    totallen = len(instr)
    # in Java you can use string builder as it's mutable
    inlst = list(instr)
    for idx in xrange(mididx):
        temp = inlst[idx]
        inlst[idx] = inlst[totallen-1-idx]
        inlst[totallen-1-idx] = temp

    print "Reverse String Method2: ", ''.join(inlst)

if __name__ == '__main__':
    reverseString('Ronaka')