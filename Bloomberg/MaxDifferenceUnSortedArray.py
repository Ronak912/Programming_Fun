# Find the maximum difference in an unsorted array with the index of max greater than min. array cant be sorted


def findMaxDifference(inlst):
    maxdifference = 0
    min_idx, max_idx = 0, 0
    for idx, val in enumerate(inlst):
        if idx == 0:
            continue

        if val < inlst[min_idx]:
            min_idx = idx
        if val > inlst[max_idx]:
            max_idx = idx
        if max_idx > min_idx and (inlst[max_idx] - inlst[min_idx] > maxdifference):
            maxdifference = inlst[max_idx] - inlst[min_idx]

    return maxdifference


if __name__ == "__main__":
    print findMaxDifference([10, 5, 11, 2, 8, 25, 15, 30])
    print findMaxDifference([10, 5, 11, 2, 3, 4, 5, 1])