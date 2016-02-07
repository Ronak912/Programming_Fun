import itertools

square = lambda x: x*x

print map(square, [1,2,3,4,5,6])
mapgen = itertools.imap(square, [1,2,3,4,5,6])
for val in mapgen:
    print val


# Filter
iseven = lambda x: x % 2 == 0
print filter(iseven, [1,2,3,4,5,6])
for val in itertools.ifilter(iseven, [1,2,3,4,5,6]):
    print val


# Reduce
sum = lambda x, y: x+y
print reduce(sum, [1, 2, 3, 4, 5, 6])
