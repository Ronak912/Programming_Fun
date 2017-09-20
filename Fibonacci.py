# Questions related to Fibonacci

# There is a row of stones leading across a river; you can either step to the next stone or skip that one;
# how many possible sequences are there to get across the river with n stones

def fibonacci(n):
    fib = [0] * (n+1)
    for i in xrange(0, n+1):
        if i <= 1:
            fib[i] = i
        else:
            fib[i] = fib[i-1] + fib[i-2]
    print ' '.join([str(val) for val in fib])



if __name__ == "__main__":
    fibonacci(10)