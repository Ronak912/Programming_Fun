
memo= {}
def fib(n):
    global memo

    if n in memo:
        print "inside"
        return memo[n]

    if n == 0 or n == 1:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
        memo[n] = f
    return f

print fib(14)