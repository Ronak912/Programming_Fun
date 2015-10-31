def run_prog():
    ONE = "one"
    MORE = 'more'

    inputstr = "teeterr ronak rkao"
    hastbl = {}
    for char in inputstr:
        if char not in hastbl:
            hastbl[char] = ONE
        else:
            hastbl[char] = MORE


    for char in inputstr:
        val = hastbl.get(char, '')
        if val == ONE:
            print "First Non Repeated Char is: ", char, "   ", val
            break


if __name__ == '__main__':
    run_prog()