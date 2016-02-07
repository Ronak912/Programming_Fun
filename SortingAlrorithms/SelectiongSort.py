lst = [1,6,4,9,10,2,3]

totallen = len(lst)

def swap(lst, i, j ):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

# Selection Sort
for i in xrange(totallen):
    currmin = i
    for j in xrange(i+1, totallen):
        currmin = j if lst[j] < lst[currmin] else currmin
    swap(lst, i, currmin)

print "Sorted Array: ", lst