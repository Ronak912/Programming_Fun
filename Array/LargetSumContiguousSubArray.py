# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers
# which has the largest sum.

# ex: lst = [-2, -3, 4, -1, -2, 1, 5, -3]
# Answer: Maximum sum is for subarray [4, -1, -2, 1, 5] = 7


def getMaxSubArraySum(lst):

    maxsofar, currsum = lst[0], lst[0]
    for val in lst[1:]:
        currsum = max(val, currsum+val)
        maxsofar = max(maxsofar, currsum)
    return "Max sum of subarray is {}".format(maxsofar)


if __name__ == "__main__":
    print(getMaxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]))





