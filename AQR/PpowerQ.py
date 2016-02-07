#Write a function that takes as input integers P and Q and returns P to the power of Q.  Note any

#assumptions you make and the complexity of the algorithm.  We expect you to do better than O(Q).


#p^Q
def pPowerQ(p, q):
    ans = 1
    while q > 0:
        ans *= p
        q -= 1
    return ans


if __name__ == '__main__':
    print pPowerQ(2, 3)

