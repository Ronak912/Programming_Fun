from SortingAlrorithms import QuickSort

totallen = None
medianvals = []

def findMedian(alist1):
    global totallen
    totallen = len(alist1)
    #print "Middle Idx: ", totallen //2
    return quickSortHelper(alist1, 0, len(alist1)-1)


def quickSortHelper(alist1, first, last):
    global totallen, medianvals
    print first, last

    if first == last:
        if totallen % 2 != 0 and totallen//2 == first:
            print "inside"
            medianvals = [alist1[first]]
        elif totallen % 2 == 0 and (totallen//2 == first or (totallen//2)-1 == first):
            print "here"
            medianvals.append(alist1[first])
        return
    elif first >= last:
        return

    splitpoint = QuickSort.partition(alist1, first, last)

    if totallen % 2 != 0 and totallen//2 == splitpoint:
        print "inside: ", splitpoint
        medianvals = [alist1[splitpoint]]
    elif totallen % 2 == 0 and (totallen//2 == first or (totallen//2) - 1 == first):
        medianvals.append(alist1[first])

    quickSortHelper(alist1, first, splitpoint-1)
    quickSortHelper(alist1, splitpoint+1, last)

if __name__ == "__main__":
    alist1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 33]
    alist2 = alist1[:]
    QuickSort.quickSort(alist2)
    print alist2
    findMedian(alist1)
    print medianvals
    #print(alist)