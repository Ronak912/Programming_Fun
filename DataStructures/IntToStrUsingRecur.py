import Stack

stack = Stack.Stack()

def intToStr(innum):
    if innum <= 9:
        return str(innum)
    else:
        return intToStr(innum // 10) + str(innum % 10)


def intToStrUsingStck(innum):

    while innum > 0:
        lastdigit = str(innum % 10)
        innum = innum // 10
        stack.push(lastdigit)
    res = ''
    while not stack.isEmpty():
        res += str(stack.pop())
    print res


#intToStrUsingStck(9234)
print intToStr(9234)