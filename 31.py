def run_prog(maxnumber):
    FIZ = "FIZZ"
    BUZ = "BUZZ"
    FIZBUZ = "FIZZBUZZ"

    print '\n'.join(FIZBUZ if i%3==0 and i%5==0 else FIZ if i%3==0 else BUZ if i%5==0 else str(i) for i in xrange(1, maxnumber+1))

    # for i in xrange(1, maxnumber+1):
    #     if i%3 == 0 and i%5 == 0:
    #         print FIZBUZ
    #     elif i%3 == 0:
    #         print FIZ
    #     elif i%5 == 0:
    #         print BUZ
    #     else:
    #         print i


if __name__ == '__main__':
    run_prog(20)