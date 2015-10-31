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

print firstNonRepeatedChar("ronakonkxgr")


