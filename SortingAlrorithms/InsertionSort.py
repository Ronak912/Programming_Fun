lst = [1,6,4,9,10,2,3]

totallen = len(lst)

# Insertion Sort
for i in xrange(1, totallen):
    currval = lst[i]
    j = i
    while j > 0 and lst[j-1] >= currval:
        lst[j] = lst[j-1]
        j -= 1
    lst[j] = currval

print "Sorted Array: ", lst