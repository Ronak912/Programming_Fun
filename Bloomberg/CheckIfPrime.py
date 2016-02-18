import math


def isPrime(n):
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print isPrime(17)
    print isPrime(50)