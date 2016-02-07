# http://www.geeksforgeeks.org/group-multiple-occurrence-of-array-elements-ordered-by-first-occurrence/
#
# Group multiple occurrence of array elements ordered by first occurrence
# Given an unsorted array with repetitions, the task is to group multiple occurrence of individual elements. The grouping should happen in a way that the order of first occurrences of all elements is maintained.
#
# Examples:
#
# Input: arr[] = {5, 3, 5, 1, 3, 3}
# Output:        {5, 5, 3, 3, 3, 1}
#
# Input: arr[] = {4, 6, 9, 2, 3, 4, 9, 6, 10, 4}
# Output:        {4, 4, 4, 6, 6, 9, 9, 2, 3, 10}

def groupElements(inlst):
    disvallst = []
    hashmap = {}
    for val in inlst:
        if val not in hashmap:
            hashmap[val] = 1
        else:
            hashmap[val] = hashmap[val] + 1

    reslst = []
    for value in inlst:
        count = hashmap.get(value, 0)
        if count:
            for i in xrange(count):
                reslst.append(value)
            del hashmap[value]
    return reslst

if __name__ == '__main__':
    print groupElements([5, 3, 5, 1, 3, 3])
    print groupElements([4, 6, 9, 2, 3, 4, 9, 6, 10, 4])