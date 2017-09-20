# https://www.careercup.com/question?id=5684774451544064

# You are given an array of values, (not necessary integers or positives) and a value. You have to print all
# the pairs whose sum is given value. Write a general method which can accept integers, float, doubles, long, or any other
# thing where this make sense.


def findAllValuesUsingSort(lst, sumval):
    lstsorted = sorted(lst)
    i = 0
    j = len(lstsorted) - 1
    outputlst = []
    while i < j:
        totalsum = lstsorted[i] + lstsorted[j]
        if totalsum == sumval:
            outputlst.append((lstsorted[i], lstsorted[j]))
            i += 1
            j -= 1
        elif totalsum < sumval:
            i += 1
        else:
            j -=1
    return outputlst

def findAllValuesUsingHashmap(lst, sumval):
    hashmap = {val: True for val in lst}
    outputlst = []
    for value in hashmap:
        # this is to make sure we do duplicate pairs, ex: (7,20) and (20,7)
        hashmap[value] = False
        desireval = sumval - value
        if hashmap.get(desireval, False):
            outputlst.append((value, desireval))

    return outputlst



if __name__ == "__main__":

    arr = [1, 5, 67, 45, 34, 23, 6, 8, 9, 40, 23, 90, 76, 43, 18, 7, 20, 15, 12]
    k = 27
    print findAllValuesUsingSort(arr, k)
    print findAllValuesUsingHashmap(arr, k)



