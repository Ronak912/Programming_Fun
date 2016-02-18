# http://www.careercup.com/question?id=5753545955475456


def FindPairs(lst, sum):
    hastset = {}
    for val in lst:
        remainingval = sum - val
        if remainingval in hastset:
            print val, "==", remainingval
        else:
            hastset[val] = True


if __name__ == '__main__':
    FindPairs([1, 2, 3, 5, 5, 9, 8], 10)