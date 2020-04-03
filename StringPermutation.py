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

# http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
def permute(a, l, r):
    if l==r:
        print ''.join(a),
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

def numPermute(nums):
    res = []

    if len(nums) == 1:
        res.append(nums)
        return res

    for i in range(len(nums)):
        for perm in numPermute(nums[:i] + nums[i+1:]):
            res.append([nums[i]] + perm)
    return res

print permute2('abc')
print "====second method==="
string = 'abc'
permute(list(string), 0, len(string)-1)
print ''
print ''
print(numPermute([1,2,3]))