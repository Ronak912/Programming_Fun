import itertools

def test(num):

    tmpnum = num
    numASlst = []
    while tmpnum > 0:
        numASlst.append(tmpnum % 10)
        tmpnum /= 10

    #print numASlst

    totalsimilarnum = 0
    totaldigit = len(numASlst)

    distinctnum = set([num])

    for item in itertools.permutations(numASlst):
        if item[0] == 0:
            continue
        tmpnum = 0
        #print item
        for idx in range(totaldigit):
            curridx = totaldigit-(idx+1)
            tmpnum += item[curridx] * (10 ** idx)
        distinctnum.add(tmpnum)

    print len(distinctnum)

test(100)

# gen = itertools.permutations([4,5,6])
# for i in gen:
#     print i





