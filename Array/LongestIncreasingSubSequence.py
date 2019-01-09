# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

# Also checkout Bloomberg/LongestIncreasingSubSequence.py
# Dynamic programming
def getLongestIncreasingSubSequence(arr):
    n = len(arr)
    l = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and l[i] < l[j]+1:
                l[i] = l[j] + 1

    maxlen = -1
    for val in l:
        maxlen = max(maxlen, val)

    print(l)
    print("Longest Incresing SubSequence is: ", maxlen)

if __name__ == "__main__":
    lst = [10, 22, 9, 33, 21, 50, 41, 60]
    getLongestIncreasingSubSequence(lst)