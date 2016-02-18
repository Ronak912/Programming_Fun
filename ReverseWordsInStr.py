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

def reverseWordusingStack(instr):
    tmpstr = ''
    stack = []
    for idx, char in enumerate(instr):
        if idx == len(instr)-1:
            if idx != ' ':
                tmpstr += char
            stack.append(tmpstr)
        elif idx == 0 and char == ' ':
            continue
        elif char == ' ':
            stack.append(tmpstr)
            tmpstr = ''
        else:
            tmpstr += char

    revstr = ''
    while stack:
        revstr += stack.pop()
        revstr += ' ' if len(stack) > 0 else ''

    return revstr


if __name__ == "__main__":
    ans = reverseWords("Where are you Ronak")
    print "Output: ", ans
    print "Using Stack: ", reverseWordusingStack("Where are you Ronak")

