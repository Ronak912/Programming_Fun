# Program to count vowels in a string (Iterative and Recursive)
# http://www.geeksforgeeks.org/program-count-vowels-string-iterative-recursive/


def countVowelsIter(instr):
    count = 0

    for char in instr:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return count


def isVowel(char):
    if char.lower() in ('a', 'e', 'i', 'o', 'u'):
        return 1
    return 0

def countVowelsRecur(instr, n):
    if n < 1:
        return 0
    return countVowelsRecur(instr, n-1) + isVowel(instr[n-1])


if __name__ == "__main__":
    instr = "ronak_agrawal"
    print countVowelsIter(instr)
    print countVowelsRecur(instr, len(instr))
