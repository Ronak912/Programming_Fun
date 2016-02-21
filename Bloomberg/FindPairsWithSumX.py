# http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/

# Given an int array int list = {4,5,6,1,2,...} and an integer int target = 8
# Write a function to return all the pairs (x, y) in the integer array that x + y = target (remove the duplicate one)

def findPairs(inlst, sumx):
    #use more sophisticated sort ex: quicksort
    inlst.sort()
    print inlst
    left = 0
    right = len(inlst)-1
    pairlst = []
    while left <=right:
        currsum = inlst[left] + inlst[right]
        if currsum == sumx:
            pairlst.append((inlst[left], inlst[right]))
            left += 1
            right -= 1
        elif currsum < sumx:
            left += 1
        else:
            right -= 1

    return pairlst


if __name__ == "__main__":
    print findPairs([1, 8, 2, 7, 3, 6, 4, 6, 6], 8)