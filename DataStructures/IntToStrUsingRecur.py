import Stack

stack = Stack.Stack()

def intToStr(innum):
    dividednum = innum // 10
    if dividednum < 1:
        return str(innum)
    else:
        intToStr(innum // 10) + str(innum % 10)


def intToStrUsingStck(innum):

    while innum > 0:
        lastdigit = str(innum % 10)
        innum = innum // 10
        stack.push(lastdigit)
    res = ''
    while not stack.isEmpty():
        res += str(stack.pop())
    print res


intToStrUsingStck(1234)