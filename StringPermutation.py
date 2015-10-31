def permute2(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            #print "First: ", i,"==",c
            for perm in permute2(s[:i] + s[i+1:]):
                res += [c + perm]
                #print "sec: ", c, "===", perm, "===", res

    #print "res: ", s, "===", res
    return res

print permute2('abc')