def getstring(instr):
    outputstr = ''
    count = 1
    if len(instr) == 1:
        print(instr+'1')
        return
    for i in xrange(1, len(instr)):
        if instr[i] == instr[i-1]:
            count += 1
        else:
            outputstr += instr[i-1] + str(count)
            count = 1
        if i == len(instr)-1:
            outputstr += instr[i] + str(count)
    print(outputstr)


if __name__ == "__main__":
    getstring('aaabbcc')