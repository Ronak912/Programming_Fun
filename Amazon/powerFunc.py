from itertools import repeat
def powCust(a, b):
    return reduce(lambda x, y: x*y, repeat(a,b))

if __name__ == "__main__":
    print powCust(2, 3)