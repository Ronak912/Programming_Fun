# http://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/

# Given two strings A and B, the task is to convert A to B if possible. The only operation allowed is to put any
#     character from A and insert it at front. Find if it is possible to convert the string. If yes, then output minimum
#     no. of operations required for transformation.

# Input:  A = "ABD", B = "BAD"
# Output: 1
# Explanation: Pick B and insert it at front.
#
# Input:  A = "EACBD", B = "EABCD"
# Output: 3
# Explanation: Pick B and insert at front, EACBD => BEACD
#              Pick A and insert at front, BEACD => ABECD
#              Pick E and insert at front, ABECD => EABCD


def transformStrings(str1, str2):

    m = len(str1)
    n = len(str2)
    if m != n:
        return -1

    hashmap = {}
    for char in str1:
        hashmap[char] = hashmap.get(char, 0) + 1

    for char in str2:
        count = hashmap.get(char, 0)
        if count == 1:
            del hashmap[char]
        else:
            hashmap[char] -= 1
    if hashmap:
        print "Characters do not match"
        return -1
    i, j = m-1, n-1
    steps = 0
    while i >= 0:
        while i >= 0 and str1[i] != str2[j]:
            i -= 1
            steps += 1
        i -= 1
        j -= 1
    return steps


if __name__ == '__main__':
    print "Total Steps Required: ", transformStrings('ABCDE', 'BCEAD')
    # Not Possible
    print "Total Steps Required: ", transformStrings('ABCDE', 'BCEADD')
    # Identical Strings
    print "Total Steps Required: ", transformStrings('ABCDE', 'ABCDE')
