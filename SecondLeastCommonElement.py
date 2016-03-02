
def secondLeastCommon(inlst):
    hashmap = {}
    for val in inlst:
        if val not in hashmap:
            hashmap[val] = 1
        else:
            hashmap[val] = hashmap[val] + 1

    print hashmap
    return list(sorted(hashmap.items(), key=lambda x: x[1]))[1]


if __name__ == '__main__':
    print secondLeastCommon([1, 2, 3, 4, 5, 5, 4, 4, 3, 3, 2, 1, 1, 1, 3, 5, 5])