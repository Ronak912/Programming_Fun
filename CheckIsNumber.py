"""
    Check if given input string is number or not without using any inbuilt mathods
"""
import re

def checkNumber1(inputstr):
    pattern = "^(-)?[0-9]+(\\.)?[0-9]+$"
    p1 = re.compile(pattern)

    m = p1.match(inputstr)
    return True if m else False


def isNumber2(inputstr1):
    totaln = len(inputstr1)
    metdot = False

    for i in range(totaln):
        c = inputstr1[i]
        if c < '0' or c > '9':
            if i == 0 and (c == '-' or c == '+'):
                continue
            elif i > 0 and i < totaln -1 and c == '.' and not metdot:
                metdot = True
                continue
            return False
    return True



def isNumber(inputstr):
    if not inputstr:
        return None

    isnumber = True
    for char in inputstr:
        if char < '0' or char > '9':
            isnumber = False
            break

    return isnumber

print isNumber('123456')
print checkNumber1('-12.345678hjkk')
print isNumber2('+2342341.3244234')