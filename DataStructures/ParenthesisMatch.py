import Stack

def matchParen(inputstr):
    stack = Stack.Stack()
    for char in inputstr:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if not stack.getsize():
                return False
            prevchar = stack.pop()
            if (prevchar == '(' and char != ')') or  \
                (prevchar == '{' and char != '}')  or \
                (prevchar == '[' and char != ']'):
                return False

    if stack.getsize() > 0:
        return False
    return True



if __name__ == "__main__":
    # valid
    print matchParen("(hi{ronak}[what are] you) {doing}")
    # invalid
    print matchParen("(hi{ronak}[what are] you) {doing}]")