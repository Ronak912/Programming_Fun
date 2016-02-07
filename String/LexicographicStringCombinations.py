

outlst = []

# def combine(s, i, j):
#     return s[i]+s[j]

def buildSubsequences( s):
    for i in xrange(len(s)):
        outlst.append(s[i])
        for j in xrange(i+1, len(s)):
            outlst.append(s[i]+s[j])

        r = i+1
        while r < len(s):
            p = r
            while p < len(s):
                q = 2
                while (i+q) <=len(s):
                    tmpstr = s[i] + s[p:p+q]
                    if tmpstr not in outlst:
                        outlst.append(tmpstr)
                    q += 1
                p += 1
            r += 1

    # outlst.append(s)
    print sorted(outlst)


buildSubsequences('abcde')