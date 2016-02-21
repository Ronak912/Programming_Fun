# Given a array of a series of characters (char array from string) reduce multiple spaces to a single space,
# while preserving the other characters. The swapping needs to take place within the initial array.

def removeMultipleSpaces(instr):
    try:
        straslst = list(instr)
        read, write = 0, 0
        while read < len(straslst):
            # check if current value is white space and if it is then last entry should not be white space
            if straslst[read] != ' ' or straslst[write-1] != ' ':
                straslst[write] = straslst[read]
                write += 1
            read += 1

        # need flush all other values after write index, so slices array here
        return ''.join(straslst[0:write])
    except Exception, ex:
        print "error"
        print ex.__str__()


if __name__ == "__main__":
    instr = 'ronak  how     are you'
    print removeMultipleSpaces(instr)