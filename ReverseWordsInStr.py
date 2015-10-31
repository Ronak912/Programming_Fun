def reverseWords(inputstr):
    lst = []
    tmpword = ''
    count = 1
    for char in inputstr:
        if char == ' ':
            lst.append(tmpword)
            tmpword = ''
        elif count == len(inputstr):
            tmpword += char
            lst.append(tmpword)
        else:
            tmpword += char
        count += 1

    newstr = ''
    while lst:
        newstr += lst.pop() + ' '
    return newstr[:-1]

if __name__ == "__main__":
    ans = reverseWords("Where are you Ronak")
    print "Output: ", ans

