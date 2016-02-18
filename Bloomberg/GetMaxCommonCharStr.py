# http://www.careercup.com/question?id=6431075731505152
# Write a program to accept a nonempty string of alphanumeric characters. Define a "run" as a
#
# consecutive sequence of a single character. For example, "aaaa" is a run of length 4. The program will
#
# print the longest run in the given string. If there is no single longest run, then you may print any of
#
# those runs whose length is at least as long as all other runs in the string.
#
# Example input: a
#
# Example output: a
#
# Example input: aab
#
# Example output: aa
#
# Example input: abbbbbcc
#
# Example output: bbbbb
#
# Example input: aabbccdd
#
# Example output: aa


def getMaxStr(instr):
    curchar = instr[0]
    currentrun = 1
    maxrun = 1
    for idx in xrange(1,len(instr)):
        if instr[idx] == instr[idx-1]:
            currentrun += 1
            if currentrun > maxrun:
                curchar = instr[idx]
                maxrun = currentrun
        else:
            currentrun = 1

    return ''.join([curchar for x in range(maxrun)])



if __name__ == "__main__":
    # we can do this using hashmap also
    print getMaxStr('aabbbccccdd')

