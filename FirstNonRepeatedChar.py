#from collections import OrderedDict

"""
From python 2.7 there is a OrderedDict which maintain orders
"""

def firstNonRepeatedChar(inputstr):
    tmplst = []
    tmpdict = {}

    for char in inputstr:
        if char in tmpdict:
            tmpdict[char] += 1
        else:
            tmpdict[char] = 1
            tmplst.append(char)

    for char in tmplst:
        if tmpdict[char] == 1:
            return char

    return None

def firstNonRepeatedChar1():
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

print firstNonRepeatedChar("ronakonkxgr")


