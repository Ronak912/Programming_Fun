# http://www.geeksforgeeks.org/sieve-of-eratosthenes/
# Sieve of Eratosthenes

# Get all prime Numbers between 1 to n

import math


def getAllPrimeNumbers(n):

    primelst = [True for i in xrange(n+1)]
    p = 2
    while p <= int(math.sqrt(n)):
        # means it's marked and hence not a prime number
        if not primelst[p]:
            p += 1
            continue
        for i in xrange(p*2, n+1, p):
            primelst[i] = False
        p += 1

    return ", ".join([str(idx) for idx, val in enumerate(primelst) if idx >= 2 and val is True])


if __name__ == "__main__":
    print getAllPrimeNumbers(40)