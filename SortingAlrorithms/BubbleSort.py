lst = [1,6,4,9,10,2,3]

totallen = len(lst)

def swap(lst, i, j ):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

# Bubble Sort
for i in xrange(totallen):
    for j in xrange(i+1, totallen):
        if lst[i] > lst[j]:
            swap(lst, i, j)

print "Sorted Array: ", lst