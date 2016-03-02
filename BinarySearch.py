

def binarySearchRecur(inlst, item):
    if len(inlst) == 0:
        return False
    mid = len(inlst) / 2

    if item == inlst[mid]:
        return mid
    elif inlst[mid] < item:
        binarySearchRecur(inlst[mid+1:], item)
    else:
        binarySearchRecur(inlst[:mid], item)
    return False

def binarySearchIter(inlst, item):
    if len(inlst) == 0 or (len(inlst) == 1 and inlst[0] != item):
        return False

    start = 0
    end = len(inlst)-1
    left = start
    right = end
    while True:
        if left == right and inlst[left] != item:
            return False
        mid = (left + right)/2
        if inlst[mid] == item:
            return mid
        elif inlst[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9]
    # print binarySearchRecur(lst, 14)
    print binarySearchIter(lst, 7)