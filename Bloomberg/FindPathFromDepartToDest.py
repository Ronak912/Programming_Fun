# http://www.careercup.com/question?id=5768610725232640

# Good day I just got a question which is the following
#
# you have an vector like this
#
# [JFK, LXA, SNA, RKJ, LXA, SNA]
# each 2 group define a route. so,
#
# JFK -> LXA
# SNA -> RKJ
# LXA -> SNA
# Find the path from departure to destination. note: departure and destination are not known.
#
# The final destination should be
#
# JFK-> LXA -> SNA -> RKJ
# The function signature is something like this
#
# vector<string> findPath(vector<string> airports)
# {
#
# }
#
# The airports (nodes) cannot be duplicated and the path should print all the airports (nodes)


def findPath(inlst):
    hashmap = {}
    fromset = set([])
    for i in xrange(0, len(inlst)-1, 2):
        fromset.add(inlst[i+1])
        hashmap[inlst[i]] = inlst[i+1]

    start = ''
    for key, val in hashmap.iteritems():
        if key not in fromset:
            start = key
            break

    outlst = []
    while start:
        outlst.append(start)
        start = hashmap.get(start, '')

    return '->'.join(outlst)

if __name__ == '__main__':
    print findPath(['JFK', 'LXA', 'SNA', 'RKJ', 'LXA', 'SNA'])
