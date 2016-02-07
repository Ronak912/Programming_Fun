# http://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/#disqus_thread
# https://ideone.com/IO9hw2

# Input: arr[] = {9, 7, 5, 3}, k = 6
# Output: True
# We can divide array into (9, 3) and (7, 5).
# Sum of both of these pairs is a multiple of 6.
#
# Input: arr[] = {92, 75, 65, 48, 45, 35}, k = 10
# Output: True
# We can divide array into (92, 48), (75, 65) and
# (45, 35). Sum of all these pairs is a multiple of 10.
#
# Input: arr[] = {91, 74, 66, 48}, k = 10
# Output: False


def isArrayDividable(lst, k):

    if len(lst) % 2 != 0:
        return False

    newset = set()
    for val in lst:
        remainder = val % k
        if (k - remainder) in newset:
            newset.remove(k-remainder)
        else:
            newset.add(remainder)
    return len(newset) == 0


if __name__ == "__main__":
    lst = [5, 4, 6, 3, 10, 8]
    print isArrayDividable(lst, 9)