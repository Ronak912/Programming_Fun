# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

"""Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
    If there is such a triplet present in array, then print the triplet and return true. Else return false.
    For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
    then there is a triplet (12, 3 and 9) present in array whose sum is 24."""

__author__ = 'Ronak'

def findTriplet1(arr, sum):
    """
    Time Complexity O(n^2), Space complexity O(logN)
    Sort array and traverse 2 loops
    """
    arr = sorted(arr)
    print(arr)
    size = len(arr)

    for i in range(size-2):
        currval = arr[i]
        l = i+1
        r = size-1
        while l < r:
            if currval+arr[l]+arr[r] == sum:
                return (currval, arr[l], arr[r])
            elif currval+arr[l]+arr[r] > sum:
                r -=1
            else:
                l +=1
    return None


def findTriplet2(arr, sum):
    """ using hashing """
    size = len(arr)
    for i in range(size-1):
        s = set()
        cumsum = sum - arr[i]
        for j in range(i+1, size):
            if cumsum-arr[j] in s:
                return (arr[i], arr[j], cumsum-arr[j])
            else:
                s.add(arr[j])
    return None




if __name__ == "__main__":
    arr = [12, 3, 4, 1, 6, 9]
    sum = 24
    triplet = findTriplet1(arr, sum)
    print(triplet)
    # Below solution is more efficient but requires O(N) extra space for hashing
    triplet2 = findTriplet2(arr, sum)
    print(triplet2)
