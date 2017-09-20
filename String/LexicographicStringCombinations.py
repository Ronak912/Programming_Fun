

outlst = []

# def combine(s, i, j):
#     return s[i]+s[j]

def buildSubsequences( s):
    for i in xrange(len(s)):
        outlst.append(s[i])

        p = i + 1
        while p < len(s):
            q = 1
            while (i+q) <=len(s):
                tmpstr = s[i] + s[p:p+q]
                if tmpstr not in outlst:
                    outlst.append(tmpstr)
                q += 1
            p += 1

    # outlst.append(s)
    print sorted(outlst)


buildSubsequences('abcde')
# ['a', 'ab', 'abc', 'abcd', 'abcde', 'ac', 'acd', 'acde', 'ad', 'ade', 'ae', 'b', 'bc', 'bcd', 'bcde', 'bd', 'bde', 'be', 'c', 'cd', 'cde', 'ce', 'd', 'de', 'e']