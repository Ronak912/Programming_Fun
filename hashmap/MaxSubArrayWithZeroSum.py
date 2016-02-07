# http://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

# Find the largest subarray with 0 sum
# Given an array of integers, find length of the largest subarray with sum equals to 0.
#
# Examples:
#
# Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
# Output: 5
# The largest subarray with 0 sum is -2, 2, -8, 1, 7
#
# Input: arr[] = {1, 2, 3}
# Output: 0
# There is no subarray with 0 sum
#
# Input: arr[] = {1, 0, 3}
# Output: 1

# ToDo: this is not proper solution and do not solve all the inputs

# Returns the maximum length
def maxLen(arr):

    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictonary)
    hash_map = {}

    # Initialize result
    max_len = 0

    # Initialize sum of elements
    curr_sum = 0

    # Traverse through the given array
    for i in range(len(arr)):

        # Add the current element to the sum
        curr_sum += arr[i]

        if arr[i] is 0 and max_len is 0:
            max_len = 1

        if curr_sum is 0:
            max_len = i+1

        # NOTE: 'in' operation in dictonary to search key takes O(1)
        # Look if current sum is seen before

        print i, "==", max_len, "==", curr_sum, "==", hash_map
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum] )
        else:
            # else put this sum in dictonary
            hash_map[curr_sum] = i

    return max_len

def maxLen1(inlst):
    inlst.sort()

    hashmap = {}
    sum, count = 0, 0
    for val in inlst:
        sum += val
        count += 1
        print val, "==", sum, "===", count
        if sum == 0:
            maxlen = max(count, hashmap.get(sum, 0))
            hashmap[sum] = maxlen


    return hashmap.get(0, 0)


if __name__ == '__main__':
    print maxLen([15, -2, 2, -12, 1, 10, 13, 8, 4,5, 12])