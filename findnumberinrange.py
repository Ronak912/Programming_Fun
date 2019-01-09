digit = 2
start = 4
end = 60

while start <=end:
    i = start
    while i > 0:
        mod = i % 10

        if digit == mod:
            print start,
            break

        i = i/10
    start += 1