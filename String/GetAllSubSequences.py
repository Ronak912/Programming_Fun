# https://www.geeksforgeeks.org/print-subsequences-string/


def getAllSubSequences(instr):
    outputset = set()
    n = len(instr)
    #traverse from the beginning
    for i in range(n):
        # traverse from the end
        for j in range(n, i, -1):
            substr = instr[i:j]
            outputset.add(substr)

            for k in range(1, n):
                # remove kth element
                substrtmp = substr[:k] + substr[k+1:]
                outputset.add(substrtmp)

    print(outputset)


if __name__ == "__main__":
    getAllSubSequences("abcd")