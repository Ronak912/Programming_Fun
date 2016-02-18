def floor(a, b):
    if not a or not b :
        return None
    if b == 1:
        return a
    sign = 1 if a > 0 else -1
    count = 0
    while True:
        if a >= 0:
            a -= b
            if a < 0:
                break
        else:
            a = a + b  # a is -ve number so add b to reach to zero
            # a = -a
            if a > 0:
                count += 1
                break
        count += 1
    return count*sign

if __name__ == "__main__":
    print floor(13, 2)
    print floor(-13, 2)