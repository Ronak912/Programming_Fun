"""
input: "Ronak What are you doing"
output1: "doing you are What Ronak"
#output2: "kanoR tahW era uoy gniod"
"""

def reverseString(intputstr):
    newlst = []
    for i in xrange(len(intputstr)-1, -1, -1):
        newlst.append(intputstr[i])
    return ''.join(newlst)


def reverseWords(inputstr):
    revstr = reverseString(inputstr)
    outputstr = ''
    tmpstr = ''
    for i, char in enumerate(revstr):
        if char == ' ':
            outputstr += reverseString(tmpstr) + ' '
            tmpstr = ''
        elif i == len(revstr) - 1:
            tmpstr += char
            outputstr += reverseString(tmpstr)
        else:
            tmpstr += char

    return outputstr

# def reverseString1(intputstr):
#     startidx = 0
#     endidx = len(intputstr) - 1
#     firstpart, secondpart = '', ''
#     while startidx < endidx:
#         firstpart += intputstr[endidx]
#         secondpart = intputstr[startidx] + secondpart
#         startidx += 1
#         endidx -= 1
#     #This won't return middle element for odd length of string
#     return firstpart + secondpart

#print reverseString('ronaka')
print reverseWords('Ronak What are you doing')






