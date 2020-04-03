

def powIter(num, p):
    res = 1
    while p > 0:
        res *= num
        p -= 1
    return res

def powRecur(num, p):
    if p == 0:
        return 1

    return num * powRecur(num, p-1)

if __name__ == "__main__":
    print(powIter(5,3))
    print(powRecur(5, 3))