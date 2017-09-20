import itertools

square = lambda x: x*x

print map(square, [1, 2, 3, 4, 5, 6])
mapgen = itertools.imap(square, [1, 2, 3, 4, 5, 6])
for val in mapgen:
    print val


# Filter
iseven = lambda x: x % 2 == 0
print filter(iseven, [1, 2, 3, 4, 5, 6])
for val in itertools.ifilter(iseven, [1, 2, 3, 4, 5, 6]):
    print val


# Reduce
sum = lambda x, y: x+y
print reduce(sum, [1, 2, 3, 4, 5, 6])


def filter_func(val):
    return val % 2 == 0

print filter(filter_func, [1,2,3,4])


# Default value for mutable
# notice when you call it second time, it will extend list which was created on first call
def funcSample(n = []):
    n.extend([1, 2, 3])
    print n

print "Func Sampleeee"
funcSample()
funcSample()
