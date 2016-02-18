

import random

# Total take O(N) + O(N) = O(N) times to run
def sortArray(arr):

    hashmap = {}
    # takes O(N) to run
    for num in arr:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] = hashmap[num] + 1

    resultarr = []
    # takes O(N) to run
    for number in sorted(hashmap):
        counter = hashmap[number]
        for i in xrange(counter):
            resultarr.append(number)

    return resultarr


if __name__ == '__main__':
    arr = []
    # Generate random number between 1 to 10
    for val in xrange(100):
        arr.append(random.randint(1, 10))
    sortedarr = sortArray(arr)
    print "Total Length: ", len(sortedarr)
    print sortedarr